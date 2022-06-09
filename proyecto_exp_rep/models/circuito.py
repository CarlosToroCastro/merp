# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Circuito(models.Model):

	_name = 'ct.circuito'
	_description = 'Circuito'

	def name_get(self):
		""" Personalizar nombre a mostrar en campos de seleccion"""
		result = []
		for record in self:
			name = "[%s] %s " % (record.codigo, record.name)
			result.append([record.id, name])
		return result

	@api.model
	def name_search(self, name="", args=None, operator="ilike", limit=100):
		""" Permitir buscar por codigo """
		domain = args or []
		domain += ["|", ("name", operator, name), ("codigo", operator, name)]
		return self.search(domain, limit=limit).name_get()

	codigo = fields.Char('Código del circuito', required=True)
	name = fields.Char('Nombre del circuito', required=True)
	city_id = fields.Many2one('res.city', string='Municipio')
	subestacion_id = fields.Many2one('ct.subestacion', string="Subestación", required=True)
	notas = fields.Text('Observación')