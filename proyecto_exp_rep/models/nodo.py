# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class Nodo(models.Model):

	_name = 'ct.nodo'
	_description = 'Poste, camara de inspeción u otro tipo de nodo' 


	name = fields.Char('Nodo', required=True)
	gps_altura = fields.Float('Altitud m.s.n.m')
	gps_latitud = fields.Float('Latitud')
	gps_longitud =fields.Float('Longitud')
	direccion = fields.Char('Dirección', required=True)
	estado_revision = fields.Selection([('conforme', 'CONFORME'),('no conforme', 'NO CONFORME')])
	no_conformidad_ids = fields.Many2many('ct.no_conformidades', string='No conformidad')
	notas = fields.Text('Observación')
	activo_poste_ids = fields.One2many('ct.nodo_activo','nodo1_id', string="Activos", ondelete="cascade")
	tipo_activo_id = fields.Many2one(related='activo_poste_ids.tipo_activo_id')
	luminaria_ids = fields.One2many('ct.luminaria','nodo_id', string="Luminaria")
	usuario_ids = fields.One2many('ct.usuario','nodo_id', string="Usuario")
	proyecto_id = fields.Many2one('ct.proyecto', 'Proyecto')
	state = fields.Selection(related='proyecto_id.state')
	imagen_diseno_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Diseño', domain=[('state', '=', 'diseño')])
	imagen_replanteo_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Replanteo', domain=[('state', '=', 'replanteo')])
	imagen_ejecucion_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Ejecucion', domain=[('state', '=', 'ejecucion')])
	activos_count = fields.Integer('Activos', compute='compute_count')

	def compute_count(self):
		self.activos_count = len(self.activo_poste_ids.filtered(lambda a: a.state == self.state))


	def action_activos(self):
		self.ensure_one()
		return {
			'type': 'ir.actions.act_window',
			'name': 'Activo(s) del nodo: ' + self.name,
			'view_mode': 'tree,form',
			'res_model': 'ct.nodo_activo',
			'domain': [('nodo1_id', '=', self.id), ('state', '=', self.state)],
			'context': "{'default_nodo1_id': %d, 'default_state': '%s', 'can_edit': True}" % (self.id, self.state),
		}

	_sql_constraints = [
		('nodo_name_uniq', 'unique(proyecto_id, name)', 'El nodo ya existe en el proyecto'),
	]

	@api.onchange('estado_revision')
	def onchange_tipo(self):
		if self.estado_revision == 'conforme':
			self.no_conformidad_ids = False

	def btn_replanteo(self):

		# Solo debe pasar a estado replanteo cuando se seleccione al menos un activo
		if len(self.activo_poste_ids) == 0:
			raise ValidationError("Debe seleccior al menos un Activo para pasar de estado")

		lineas_replanteo =[]
		for activo in self.activo_poste_ids.filtered(lambda a: a.state == 'diseño'):

			lista_productos = []
			for p in activo.product_ids:
				linea_producto = {
					'product_id': p.product_id.id,
					'cantidad': p.cantidad,
					'bodega' : p.bodega,
					'tipo_product': p.tipo_product,
					'state': 'replanteo'
				}
				lista_productos.append((0,0, linea_producto))			

			nueva_linea = {
					'nodo1_id': activo.nodo1_id.id,
					'a_poste_id': activo.a_poste_id.id,
					'state1': activo.state1,
					'tarea': activo.tarea,
					'notes': activo.tarea,
					'product_ids': lista_productos,
					'state': 'replanteo' 
			}
			_logger.info('Nueva linea %s', nueva_linea)
			lineas_replanteo.append((0,0, nueva_linea))

		if lineas_replanteo:
			self.activo_poste_ids = lineas_replanteo
			self.state = 'replanteo'
				


class ActivoPosteNodo(models.Model):
#realacion  entre activos y nodos. 
	_name = 'ct.nodo_activo'
	_description = 'Activos que se encuentran en un nodo'


	nodo1_id = fields.Many2one('ct.nodo', 'name', required=True)
	proyecto_id = fields.Many2one(related='nodo1_id.proyecto_id')
	a_poste_id = fields.Many2one('ct.activo_poste', 'Activo',  required=True)
	tipo_activo_id = fields.Many2one(related='a_poste_id.tipo_activo_id')
	tipo_activo_code = fields.Char(related='a_poste_id.tipo_activo_id.code')
	state1 = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutilizado'), ('Retirado', 'Retirado')], string='Estado', required=True)
	tarea = fields.Integer('Tarea MAXIMO', required=True)
	notes = fields.Text('Observación')
	product_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'mo')]) # Mano de Obra
	product_mn_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'nuevo')]) # Material Nuevo (mn)
	product_mr_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'retirado')]) # Material Retirado (mr)
	secu_fase = fields.Many2many('ct.fases_red', string='Secuencia de Fases')
	state=fields.Selection(related='nodo1_id.state')
	can_edit = fields.Boolean(string='Puede editar', compute='_can_edit')
	bloq_encabe = fields.Boolean(default=False)

	_sql_constraints = [
		('tarea_uniq', 'unique(tarea)', 'La tarea ya existe en el proyecto'),
	]
	

	#Si existe un material o mano de obra bloquea el encabezado de activo. 
	@api.onchange("product_ids", "product_mn_ids")
	def onchange_len_product(self):
		if len(self.product_ids) != 0 | len(self.product_mn_ids) != 0 :
			self.bloq_encabe = True 
		else: 
			self.bloq_encabe = False

					

	@api.depends('nodo1_id.state')
	def _can_edit(self):
		for record in self:
			_logger.info('************ , %s', record.env.context)
			estado_nodo = record.nodo1_id.state
			record.can_edit = record.state == estado_nodo
	
	
	def buscarMaterial(self, lista, product_id):		
		pos = 0
		for elemento in lista:
			if elemento['product_id'] == product_id:
				return pos
			else:
				pos += 1
		return False


	def bt_calcular_material_nuevo(self):
		if len(self.product_ids) == 0:
				# Mensaje de error para el usuario		
			pass

		if self.product_ids:

			self.product_mn_ids = False

			material_ids = []
			for mo in self.product_ids:
				for material in mo.estructura_ids.materiales_ids:
					cantidad = material.cantidad * mo.cantidad
					
					index = self.buscarMaterial(material_ids, material.product_id.id)					
					if index:						
						_logger.info(' POSICION %s - tipo %s', index, type(index))
						material_ids[index]['cantidad'] = material_ids[index]['cantidad'] + cantidad
					else:
						vals = {'product_id': material.product_id.id, 'cantidad' : cantidad, 'tipo_product': 'nuevo'}
						material_ids.append(vals)


			materiales_agrupados_id = []
			for m in material_ids:
				materiales_agrupados_id.append((0,0, m))
			self.product_mn_ids = materiales_agrupados_id



class productActivo(models.Model):
	#cantidad de mano de obra que se puede realizar en un activo.

	_name = 'ct.product_activo' 
	_description = 'Mano de obra y materiales que se utilizada en un activo'


	activo_nodo_id = fields.Many2one('ct.nodo_activo', 'Activo')
	tipo_activo_code = fields.Char(related='activo_nodo_id.tipo_activo_code')
	product_id = fields.Many2one('product.template',string='Producto')
	estructura_product_ids = fields.Many2many(related='product_id.estructura_ids')
	valor_uni = fields.Float('valor U', default=0)
	distancia = fields.Integer('Dist', default=1)		
	can_lineas = fields.Selection([('1', 1), ('2', 2),('3', 3),('4', 4)], default = '1', string="Can lineas")
	cantidad = fields.Integer('Total', default = 1)
	estructura_ids = fields.Many2one('ct.estructura', string='Estructuras')
	vali_len_estruc = fields.Boolean(default=False)
	bodega=fields.Char('Bodega')
	tipo_product = fields.Selection([('mo', 'Mano de Obra'), ('nuevo', 'Nuevo'), ('retirado', 'Retirado'),('reutilizado','Reutilizado')], required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], string='Etapa')

	@api.constrains("cantidad")
	def _constrain_cantidad(self):
		if self.cantidad <= 0:
			raise ValidationError('Debe especificar una cantidad')

	 # Si la cantidad es 0 o un numero negativo se convierte en 1
	@api.onchange("can_lineas" , "distancia")
	def onchange_cantidad(self):
		self.cantidad = int(self.can_lineas) * self.distancia
		if self.cantidad <= 0:
			self.cantidad = 1
			return {
				"warning": {"title": "Error en Cantidad",	"message": "Debe especificar una cantidad mayor a cero" }
			}	

	#Trae el valor unitario de caracteristicas del producto. 
	@api.onchange("product_id")
	def onchange_valor_uni(self):
		if self.product_id:
			self.state = self.activo_nodo_id.state
			self.valor_uni = self.product_id.list_price
		if self.product_id.detailed_type == 'service':
			self.tipo_product = 'mo'
		elif self.product_id.detailed_type == 'product':
			self.tipo_product = 'nuevo'
		elif self.product_id.name2 == 'Retirado':
			self.tipo_product = 'retirado'





	#Si la MO tiene estructuras se vuelve requerido, si tiene una sola estructura la pone por defecto.  
	@api.onchange("product_id")
	def onchange_estruc_required(self):
		self.estructura_ids = False
		if len(self.product_id.estructura_ids) != 0:
			self.vali_len_estruc = True 
			if len(self.product_id.estructura_ids) == 1: # Si solo hay una estructura queda por defecto. 
				self.estructura_ids = self.product_id.estructura_ids
		else: 
			self.vali_len_estruc = False


class fasesRed(models.Model):
	#Secuencia de fases.

	_name = 'ct.fases_red' 
	_description = 'Secuencia de fases'


	code = fields.Char('Código', required=True)
	name = fields.Char('Fase', required=True)
	