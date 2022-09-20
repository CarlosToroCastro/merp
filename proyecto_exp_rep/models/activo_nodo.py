# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ActivoPoste(models.Model):

	_name = 'ct.activo_nodo'
	_description = 'Equipo electrico, seccionador,cuchillas, transformador, (resto de estructuras)'



	nodo_id = fields.Many2one('ct.nodo', 'name', required=True)
	proyecto_id_name = fields.Char(related='nodo_id.proyecto_id.name')
	name = fields.Char('Nombre Activo', required=True)
	tipo_activo_id = fields.Many2one('ct.tipo_activo_electrico', string="Tipo Activo", required=True)
	tipo_activo_code = fields.Char(related='tipo_activo_id.code')
	state_activo = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutilizado'), ('Retirado', 'Retirado')], string='Estado', required=True)
	tarea = fields.Integer('Tarea MAXIMO', required=True)
	serie = fields.Char('Serie')
	placa = fields.Char('Placa')
	potencia = fields.Many2one('ct.pot_trans', string='Potencia Nominal')
	voltaje = fields.Selection([('7600', '7,6 kV'), ('13200', '13,2 kV')], default='13200')
	tipo = fields.Selection([('1', 'Monofásico'), ('3', 'Trifásico')])
	notes = fields.Text('Observación')
	state=fields.Selection(related='nodo_id.state')
	secu_fase = fields.Many2many('ct.fases_red', string='Secuencia de Fases')
	product_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'mo')]) # Mano de Obra
	product_mn_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'nuevo')]) # Material Nuevo (mn)
	product_mr_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'retirado')]) # Material Retirado (mr)
	bloq_encabe = fields.Boolean(default=False)

	_sql_constraints = [
		('activo_nodo_uniq', 'unique(proyecto_id_name, name)', 'Activo ya existe'),
	]

	@api.onchange('voltaje', 'tipo')
	def onchange_tipo(self):
		if self.tipo == '3':
			self.voltaje = '13200'
			

	#Si existe un material o mano de obra bloquea el encabezado de activo. 
	@api.onchange("product_ids", "product_mn_ids")
	def onchange_len_product(self):
		if len(self.product_ids) != 0 or len(self.product_mn_ids) != 0 :
			self.bloq_encabe = True 
		else: 
			self.bloq_encabe = False


		#Al cambiar de activo borra todas las casillas. 
	@api.onchange('tipo_activo_id')
	def onchange_tip_activo(self):
		if self.tipo_activo_id:
			self.state_activo = False
			self.name = False
			self.serie = False
			self.placa = False
			self.potencia = False
			self.voltaje = False
			self.tipo = False
			self.tarea = False
		if self.tipo_activo_id.code == 'poste':
			self.name = self.nodo_id.name


	def buscarMaterial(self, lista, product_id):		
		pos = 1
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

			self.product_mn_ids.filtered(lambda mn: mn.state == self.state).unlink ()

			material_ids = []
			for mo in self.product_ids:
				if mo.state == self.state:
					for material in mo.estructura_ids.materiales_ids:
						cantidad = material.cantidad * mo.cantidad
						
						index = self.buscarMaterial(material_ids, material.product_id.id)					
						if index:						
							_logger.info(' POSICION %s - tipo %s', index, type(index))
							material_ids[index-1]['cantidad'] = material_ids[index-1]['cantidad'] + cantidad
						else:
							vals = {'state': mo.state, 'product_id': material.product_id.id, 'cantidad' : cantidad, 'tipo_product': 'nuevo', 'valor_uni': material.product_id.list_price, 'valor_tot': material.product_id.list_price * cantidad}
							material_ids.append(vals)


			materiales_agrupados_id = []
			for m in material_ids:
				materiales_agrupados_id.append((0,0, m))
			self.product_mn_ids = materiales_agrupados_id




class TipoAtivoElectrico(models.Model):

	_name = 'ct.tipo_activo_electrico'
	_description = 'Ingresan los tipos de equipos electricos utilizados en MT y BT' 
	
	code = fields.Char('Codigo Interno', required=True) 
	name = fields.Char('Nombre', required=True)	
	nivel_tension_id = fields.Many2many('ct.nivel_tension', string='Nivel Tensión',required=True)
	notas = fields.Text('Observación')

	_sql_constraints = [
		('tipo_activo_electrico_code_uniq', 'unique(code)', 'Información Repetida'),
		('tipo_activo_electrico_name_uniq', 'unique(name)', 'Información Repetida')
	]

class potTrans(models.Model):

	_name = 'ct.pot_trans'
	_description = 'Pontencia mas conocida de los transformadores'


	code = fields.Char('Codigo Interno', required=True) 
	name = fields.Char('Potencia Nominal', required=True)	

	"""class (object):"""
	"""docstring for """
	"""def __init__(self, arg):
		super(, self).__init__()
		self.arg = arg"""
