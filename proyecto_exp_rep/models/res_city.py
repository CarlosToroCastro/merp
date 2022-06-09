# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResCity(models.Model):

	_inherit = 'res.city'

	def name_get(self):
		""" Personalizar nombre a mostrar en campos de seleccion"""
		result = []
		for record in self:
			name = "%s (%s) " % (record.name, record.state_id.name)
			result.append([record.id, name])
		return result