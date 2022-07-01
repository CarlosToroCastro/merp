# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):

	_inherit = 'product.template'

	name2 = fields.Char('Descripción 2')
	tipo_activo_id = fields.Many2one('ct.tipo_activo_electrico', 'Activo')
	tipo_obra_id = fields.Selection([('electrica','ELECTRICA'), ('civil', 'OBRA CIVIL')], string="Tipo Obra")
	estructura_ids = fields.One2many('product.template.estructura', 'product_id', string='Estructuras')
