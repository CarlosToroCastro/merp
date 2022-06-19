# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Rol(models.Model):

	_name = 'ct.rol'
	_description = 'Cargo que desempeñan las pesronas'

	code = fields.Char('Cdigo interno', required=True)
	name = fields.Char('Rol', required=True)
	notas = fields.Char('Observación')

	_sql_constraints = [
		('rol_code_uniq', 'unique(code)', 'Informacion Repetida'),
		('rol_name_uniq', 'unique(name)', 'Informacion Repetida'),
	]


class Proyecto(models.Model):

	_name = 'ct.proyecto'
	_description = 'Proyecto'




	name = fields.Char('Código del Proyecto', required=True)
	tipo_proyecto_id = fields.Many2one('ct.tipo_proyecto', string='Tipo de proyecto', required=True)
	direccion = fields.Char('Dirección', required=True)
	city_id = fields.Many2one('res.city', string='Municipio', required=True)
	circuito_id = fields.Many2one('ct.circuito', string="Circuito", required=True)	
	subestacion_id = fields.Many2one(related='circuito_id.subestacion_id')
	nivel_tension_id = fields.Many2one('ct.nivel_tension', string='Nivel tension',required=True)
	contrato_id = fields.Many2one('ct.contrato', string='Contrato', required=True)
	personal_ids = fields.One2many('ct.proyecto_personal', 'proyecto_id', string="Equipo de Trabajo")
	fecha_diseño = fields.Date('Fecha inicio')
	fecha_replanteo = fields.Date('Fecha Replanteo')
	fecha_ejecucion = fields.Date('Fecha Ejecución')
	area = fields.Selection([('rural', 'Rural'), ('urbano', 'Urbano')], string='Área', required=True)
	notas = fields.Text('Observación')
	#maniobras
	#SEGUIMIENTO Y CONTROL 
	#GPS


	_sql_constraints = [
		('proyecto_name_uniq', 'unique(name)', 'El código del proyecto ya existe'),
	]


class ProyectoPersonal(models.Model):

	_name = 'ct.proyecto_personal'
	_description = 'Personas que intervienen en el ciclo del proyecto'

	proyecto_id = fields.Many2one('ct.proyecto', 'name')
	rol = fields.Many2one('ct.rol', 'name')
	partner_id = fields.Many2one('res.partner', 'Contacto')
	f_inicio = fields.Date('Fecha de Inicio')
	f_fin = fields.Date('Fecha de Fin')



