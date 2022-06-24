# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):

	_inherit = 'product.template'

	name2 = fields.Char('Descripción 2')
	nivel_tesion_id = fields.Many2many('ct.nivel_tension', string='Nivel de Tensión')
	tipo_activo_id = fields.Many2one('ct.tipo_activo_electrico', 'Activo')
	tipo_obra_id = fields.Selection([('electrica','ELECTRICA'), ('civil', 'OBRA CIVIL')], string="Tipo Obra")
	material_ids = fields.One2many('product.template.materiales', 'product_id', string='Matariales')
