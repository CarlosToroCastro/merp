"""# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TipoAtivoElectrico(models.Model):

	_name = 'ct.tipo_activo_electrico'
	_description = 'Ingresan los tipos de equipos electricos utilizados en MT y BT' 

	
	name = fields.Char('Nombre', required=True)
	code = fields.Char('Codigo Interno', required=True) 	
	notas = fields.Text('Observación')

	_sql_constraints = [
		('tipo_activo_electrico_code_uniq', 'unique(code)', 'Informacion Repetida'),
		('tipo_activo_electrico_name_uniq', 'unique(name)', 'Informacion Repetida')
	]"""
