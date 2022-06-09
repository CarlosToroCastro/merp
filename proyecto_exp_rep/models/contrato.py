# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Contrato(models.Model):

	_name = 'ct.contrato'
	_description = 'Contratos de obra electrica y obra civil'

	partner_id = fields.Many2one('res.partner', 'Empresa', required=True)
	codigo = fields.Char('Codigo de contrato', required=True)
	fecha_inicio = fields.Date('Fecha inicio', required=True)
	fecha_finalizacion = fields.Date('Fecha finalización', required=True)
	notas = fields.Text('Observación')
	state = fields.Selection([('activo', 'Activo'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], string='Estado')	