# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _

class NodoImage(models.Model):
	_name = 'ct.nodo_image'

	nodo_id = fields.Many2one('ct.nodo', string='Nodo')
	name = fields.Char('Name', required=True)
	sequence = fields.Integer(default=10, index=True)
	image_1920 = fields.Image(required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')
    
