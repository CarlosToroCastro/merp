# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):

	_inherit = 'product.template'

	def name_get(self):
		""" Personalizar nombre a mostrar en campos de seleccion"""
		result = []
		for record in self:
			name = "%s - %s - %s" % (record.default_code, record.name, record.name2 or '')
			result.append([record.id, name])
		return result

    
	name2 = fields.Char('Descripción 2')
	tipo_activo_ids = fields.Many2many('ct.tipo_activo_electrico', string='Activo')
	tipo_obra_id = fields.Selection([('electrica','ELECTRICA'), ('civil', 'OBRA CIVIL')])
	nivel_tension_ids = fields.Many2many('ct.nivel_tension', string='Nivel Tensión')
	#estructura_ids = fields.One2many('product.template.estructura', 'product_id')
	estructura_ids = fields.Many2many('ct.estructura', string='Estructuras')


	
