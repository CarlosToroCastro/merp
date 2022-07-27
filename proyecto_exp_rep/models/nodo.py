# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class Nodo(models.Model):

	_name = 'ct.nodo'
	_description = 'Poste, camara de inspeción u otro tipo de nodo' 


	name = fields.Char('Nodo', required=True)
	name2 = fields.Char('Nodo Final')
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
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')

	imagen_diseno_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Diseño')
	imagen_replanteo_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Replanteo')
	imagen_ejecucion_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Ejecucion')

	def btn_replanteo(self):

		# Solo debe pasar a estado replanteo cuando se seleccione al menos un activo
		if len(self.activo_poste_ids) == 0:
			raise ValidationError("Debe seleccior al menso un Activo para pasar de estado")

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
	a_poste_id = fields.Many2one('ct.activo_poste', 'Activo',  required=True)
	tipo_activo_id = fields.Many2one(related='a_poste_id.tipo_activo_id')
	state1 = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutilizado'), ('Retirado', 'Retirado')], string='Estado', required=True)
	tarea = fields.Integer('Tarea MAXIMO', required=True)
	notes = fields.Text('Observación')
	product_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'mo')]) # Mano de Obra
	product_mn_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', ondelete="cascade", domain=[('tipo_product', '=', 'nuevo')]) # Material Nuevo (mn)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')
	can_edit = fields.Boolean(string='Puede editar', compute='_can_edit')

	@api.depends('nodo1_id.state')
	def _can_edit(self):
		for record in self:
			estado_nodo = record.nodo1_id.state
			record.can_edit = record.state == estado_nodo

class productActivo(models.Model):
	#cantidad de mano de obra que se puede realizar en un activo.

	_name = 'ct.product_activo' 
	_description = 'Mano de obra y materiales que se utilizada en un activo'


	activo_nodo_id = fields.Many2one('ct.nodo_activo', 'Activo')
	product_id = fields.Many2one('product.template',string='Producto')
	cantidad = fields.Float('Cantidad', required=True)
	estructura_ids = fields.Many2many('ct.estructura', string='Estructuras')
	bodega=fields.Char('Bodega')
	tipo_product = fields.Selection([('mo', 'Mano de Obra'), ('nuevo', 'Nuevo'), ('retirado', 'Retirado'),('reutilizado','Reutilizado')], default='mo', required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')
    
	








###NO SIRVE PARA NADA PERO NO SE PUEDE QUITAR
class productActivo2(models.Model):
	#cantidad de mano de obra que se puede realizar en un activo.

	_name = 'product_activo' 
	_description = 'Mano de obra y materiales que se utilizada en un activo'

	cantidad = fields.Float('Cantidad', required=True)
	
###NO SIRVE PARA NADA PERO NO SE PUEDE QUITAR
class ActivoPosteNodo2(models.Model):
#realacion  entre activos y nodos. 
	_name = 'ct.nodo.activo_poste'
	_description = 'Activos que se encuentran en un nodo'

	cantidad = fields.Float('Cantidad', required=True)