# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductMateriales(models.Model):

	_name = 'product.template.materiales'

	product_id = fields.Many2one('product.template', string='Producto', required=True)
	material_id = fields.Many2one('product.template', string='Insumo/Material', required=True)
	cantidad = fields.Float('Cantidad')
	ubicacion = fields.Char('Ubicación')
	tipo = fields.Selection([('nuevo','Nuevo'), ('reutilizado', 'Reutilizado')])