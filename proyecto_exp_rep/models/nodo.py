# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class Nodo(models.Model):

	_name = 'ct.nodo'
	_description = 'Poste, camara de inspeción u otro tipo de nodo' 


	name = fields.Char(string='Nodo', required=True)
	gps_altura = fields.Float(string='Altitud m.s.n.m')
	gps_latitud = fields.Float(string='Latitud')
	gps_longitud =fields.Float(string='Longitud')
	direccion = fields.Char(string='Dirección', required=True)
	estado_revision = fields.Selection([('conforme', 'CONFORME'),('no conforme', 'NO CONFORME')], string='Conformidad')
	no_conformidad_ids = fields.Many2many('ct.no_conformidades', string='No conformidad')
	notas = fields.Text(string='Observación')
	activo_nodo_ids = fields.One2many('ct.activo_nodo','nodo_id', string="Activos")
	tipo_activo_id = fields.Many2one(related='activo_nodo_ids.tipo_activo_id')
	luminaria_ids = fields.One2many('ct.luminaria','nodo_id', string="Luminaria")
	usuario_ids = fields.One2many('ct.usuario','nodo_id', string="Usuario")
	proyecto_id = fields.Many2one('ct.proyecto', string='Proyecto')
	state = fields.Selection(related='proyecto_id.state')
	imagen_diseno_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Diseño', domain=[('state', '=', 'diseño')])
	imagen_replanteo_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Replanteo', domain=[('state', '=', 'replanteo')])
	imagen_ejecucion_ids = fields.One2many('ct.nodo_image', 'nodo_id', string='Fotos Ejecucion', domain=[('state', '=', 'ejecucion')])
	activos_count = fields.Integer(string='Activos', compute='compute_count')

	_sql_constraints = [
		('nodo_name_uniq', 'unique(proyecto_id, name)', 'El nodo ya existe en el proyecto'),
	]

	def compute_count(self):
		self.activos_count = len(self.activo_nodo_ids)
		#self.activos_count = len(self.activo_nodo_ids.filtered(lambda a: a.state == self.state))


	def action_activos(self):
		self.ensure_one()
		return {
			'type': 'ir.actions.act_window',
			'name': 'Activo(s) del nodo: ' + self.name,
			'view_mode': 'tree,form',
			'res_model': 'ct.activo_nodo',
			'domain': [('nodo_id', '=', self.id), ('state', '=', self.state)],
			'context': "{'default_nodo_id': %d, 'default_state': '%s', 'can_edit': True}" % (self.id, self.state),
		}

	@api.onchange('estado_revision')
	def onchange_tipo(self):
		if self.estado_revision == 'conforme':
			self.no_conformidad_ids = False
	
	"""def btn_replanteo(self):

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
					'nodo_id': activo.nodo_id.id,
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
			"""
			
				
class fasesRed(models.Model):
	#Secuencia de fases.

	_name = 'ct.fases_red'
	_order = "sequence asc"
	_description = 'Secuencia de fases'


	code = fields.Char(string='Código', required=True)
	name = fields.Char(string='Fase', required=True)
	sequence = fields.Integer(string='sequence', help="Sequence for the handle.")



	