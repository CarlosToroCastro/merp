# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Proyecto(models.Model):

	_name = 'ct.proyecto'
	_description = 'Proyecto'


	name = fields.Char('Código del Proyecto', required=True)
	tipo_proyecto_id = fields.Many2one('ct.tipo_proyecto', string='Tipo de proyecto', required=True)
	direccion = fields.Char('Dirección', required=True)
	city_id = fields.Many2one('res.city', string='Municipio', required=True)
	circuito_id = fields.Many2one('ct.circuito', string="Circuito", required=True)	
	subestacion_id = fields.Many2one(related='circuito_id.subestacion_id')

	nivel_tension_id = fields.Many2one('ct.nivel_tension', string='nivel tension',required=True)
	personal_ids = fields.One2many('ct.proyecto_personal', 'proyecto_id', string="Equipo de Trabajo")
	fecha_diseño = fields.Date('Fecha inicio')
	fecha_replanteo = fields.Date('Fecha Replanteo')
	fecha_ejecucion = fields.Date('Fecha Ejecución')
	tipo_red = fields.Selection([('rural', 'Rural'), ('urbano', 'Urbano')], string='Tipo de red')
	notas = fields.Text('Observación')
	#maniobras
	#GPS


class ProyectoPersonal(models.Model):

	_name = 'ct.proyecto_personal'
	_description = 'Personas que intervienen en el ciclo del proyecto'

	proyecto_id = fields.Many2one('ct.proyecto', 'name')
	rol = fields.Selection([('diseño', 'Diseñador'), ('interv', 'Interventor')], string="Rol")
	partner_id = fields.Many2one('res.partner', 'Contacto')
	f_inicio = fields.Date('Fecha de Inicio')
	f_fin = fields.Date('Fecha de Fin')