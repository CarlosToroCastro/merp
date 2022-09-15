# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Proyecto(models.Model):

	_name = 'ct.proyecto'
	_description = 'Proyecto'


	name = fields.Char('Código del Proyecto', required=True)
	tipo_proyecto_id = fields.Many2one('ct.tipo_proyecto', string='Tipo de Proyecto', required=True)
	direccion = fields.Char('Dirección', required=True)
	city_id = fields.Many2one('res.city', string='Municipio', required=True)
	circuito_id = fields.Many2one('ct.circuito', string="Circuito", required=True)	
	subestacion_id = fields.Many2one(related='circuito_id.subestacion_id')
	nivel_tension_id = fields.Many2one('ct.nivel_tension', string='Nivel Tensión',required=True)
	contrato_id = fields.Many2one('ct.contrato', string='Contrato')
	personal_ids = fields.One2many('ct.proyecto_personal', 'proyecto_id', string="Equipo de Trabajo")
	fecha_diseño = fields.Date('Fecha Diseño')
	fecha_replanteo = fields.Date('Fecha Replanteo')
	fecha_ejecucion = fields.Date('Fecha Ejecución')
	area = fields.Selection([('rural', 'Rural'), ('urbano', 'Urbano')], string='Área', required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], string='Etapa', default='diseño')
	notas = fields.Text('Observación')
	nodo_ids = fields.One2many('ct.nodo', 'proyecto_id', string="Nodos", ondelete="cascade")
	valor_mo_diseno = fields.Float('valor mano de obra diseño', compute='compute_valor', default = 0)
	valor_mn_diseno = fields.Float('valor material nuevo diseño', compute='compute_valor', default = 0)
	valor_mo_replanteo = fields.Float('valor mano de obra replanteo', compute='compute_valor', default = 0)
	valor_mn_replanteo = fields.Float('valor material nuevo replanteo', compute='compute_valor', default = 0)
	valor_mo_ejecucion = fields.Float('valor mano de obra ejecucion', compute='compute_valor', default = 0)
	valor_mn_ejecucion = fields.Float('valor material nuevo ejecucion', compute='compute_valor', default = 0)
	seg_cont_ids = fields.One2many('ct.seguimiento_control', 'proyecto_id', string="Seguimiento y control" )
	maniobras_ids = fields.One2many('ct.maniobra', 'proyecto_id', string="Maniobras" )
	anexos_ids = fields.One2many('ct.archivo_proyecto', 'proyecto_id', string="Archivos")
	nodos_count = fields.Integer('Nodos', compute='compute_count')

	

	def btn_replanteo(self):
		if len(self.nodo_ids) == 0:
			raise ValidationError("No hay nodos en este proyecto")

		for nodo in self.nodo_ids:
			for activo in nodo.activo_nodo_ids:
				lista_productos = []
				for p in activo.product_ids:
					linea_producto = {
					'product_id': p.product_id.id,
					'cantidad': p.cantidad,
					#'estructura_ids': p.estructura_ids,
					'distancia': p.distancia,
					'can_lineas': p.can_lineas,
					'tipo_product': p.tipo_product,
					'valor_uni': p.valor_uni,
					'state': 'replanteo'
					}
					lista_productos.append((0,0, linea_producto))
				if lista_productos:
					activo.product_ids = lista_productos

				lista_productos_mn = []
				for mn in activo.product_mn_ids:
					linea_producto_mn = {
					'product_id': mn.product_id.id,
					'cantidad': mn.cantidad,
					'tipo_product': mn.tipo_product,
					'valor_uni': mn.valor_uni,
					'state': 'replanteo'
					}
					lista_productos_mn.append((0,0, linea_producto_mn))
				if lista_productos_mn:
					activo.product_mn_ids = lista_productos_mn







	def compute_count(self):
		self.nodos_count = len(self.nodo_ids)

	def compute_valor(self):
		self.nodos_count = len(self.nodo_ids)

	def action_nodos(self):
		self.ensure_one()
		return {
			'type': 'ir.actions.act_window',
			'name': 'Nodo(s): ' + self.name,
			'view_mode': 'tree,form',
			'res_model': 'ct.nodo',
			'domain': [('proyecto_id', '=', self.id)],
			'context': "{'default_proyecto_id': %d}" % (self.id),
		}

	
	_sql_constraints = [
		('proyecto_name_uniq', 'unique(name)', 'El código del proyecto ya existe'),
	]


class ProyectoPersonal(models.Model):

	_name = 'ct.proyecto_personal'
	_inherit = ['mail.thread']
	_description = 'Personas que intervienen en el ciclo del proyecto'

	proyecto_id = fields.Many2one('ct.proyecto', 'name')
	rol = fields.Many2one('ct.rol', 'Rol')
	partner_id = fields.Many2one('res.partner', 'Contacto')
	f_inicio = fields.Date('Fecha de Inicio')
	f_fin = fields.Date('Fecha de Fin')



	def send_mail(self):
		# search the email template based on external id
		template_id = self.env.ref('proyecto_exp_rep.mail_asignacion_proyecto', raise_if_not_found=False)		
		if template_id:
			template_id.send_mail(self.env.user.id)			
	


class SeguimientoControl(models.Model):

	_name = 'ct.seguimiento_control'
	_description ='Visitas y actas que hacen los involucrados en las difrentes etapas del proyecto'

	f_visita = fields.Date('Fecha de la visita', required=True)
	proyecto_id = fields.Many2one('ct.proyecto', 'name')
	notas = fields.Text('Observación', required=True)
	notas1 = fields.Text('Conclusión')
	notas2 = fields.Text('No conformidades')
	personal_ids = fields.One2many('ct.personal_visita', 'seguimiento_id', string="Personas que intervienen")



class PersonalVisita(models.Model):

	_name = 'ct.personal_visita'
	_description = 'Personas que interviene en una visita'

	seguimiento_id = fields.Many2one('ct.seguimiento_control', 'notas')
	rol = fields.Many2one('ct.rol', 'Rol')
	partner_id = fields.Many2one('res.partner', 'Contacto')
	

class maniobras(models.Model):

	_name = 'ct.maniobra'
	_description = 'Maniobras necesarias para desenergizar tramo de red'


	elemento = fields.Char('Elemento', required=True)
	accion = fields.Selection([('abrir', 'ABRIR'), ('cerra', 'CERRAR'), ('abrir puentes','ABRIR PUENTES')], string='Acción', required=True)
	notas = fields.Text('Observación')
	proyecto_id = fields.Many2one('ct.proyecto', 'name')

class Rol(models.Model):

	_name = 'ct.rol'
	_description = 'Cargo que desempeñan las pesronas'

	code = fields.Char('Código interno', required=True)
	name = fields.Char('Rol', required=True)
	notas = fields.Char('Observación')

	_sql_constraints = [
		('rol_code_uniq', 'unique(code)', 'Informacion Repetida'),
		('rol_name_uniq', 'unique(name)', 'Informacion Repetida'),
	]
