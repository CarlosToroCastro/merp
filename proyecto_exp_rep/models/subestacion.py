# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Subestacion(models.Model):

	_name = 'ct.subestacion'
	_description = 'Subestaciones eléctrica'


	def name_get(self):
			""" Personalizar nombre a mostrar en campos de seleccion"""
			result = []
			for record in self:
				name = "[%s] %s " % (record.codigo, record.name)
				result.append([record.id, name])
			return result

		
	codigo = fields.Char('Código de la subestación', required=True)
	name = fields.Char('Nombre de la subestación', required=True)
	city_id = fields.Many2one('res.city', string='Municipio', required=True)
	direccion = fields.Char('Dirección')
	notas = fields.Text('Observación')

	_sql_constraints = [
		('subestacion_code_uniq', 'unique(codigo)', 'Informacion Repetida'),
		
	]
