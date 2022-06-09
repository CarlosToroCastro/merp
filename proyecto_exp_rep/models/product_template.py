# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):

	_inherit = 'product.template'

	name2 = fields.Char('Descripción')