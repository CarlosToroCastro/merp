# -*- coding: utf-8 -*-

from odoo import api, fields, models

class NivelTension(models.Model):

	_name = 'ct.nivel_tension'
	_description = 'Nivel de Tensión' 


	code = fields.Char('Codigo Interno', required=True)
	name = fields.Char('Nivel de Tensión', required=True) 	
	notas = fields.Text('Observación')
	
	_sql_constraints = [
		('nivel_tension_code_uniq', 'unique(code)', 'Informacion Repetida'),
		('nivel_tension_name_uniq', 'unique(name)', 'Informacion Repetida'),
	]