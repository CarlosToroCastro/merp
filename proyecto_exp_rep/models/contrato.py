# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Contrato(models.Model):

	_name = 'ct.contrato'
	_description = 'Contratos de obra electrica y obra civil'
	_rec_name = 'codigo' 

	def name_get(self):
		""" Personalizar nombre a mostrar en campos de seleccion"""
		result = []
		for record in self:
			name = "[%s] %s " % (record.codigo, record.name_empresa)
			result.append([record.id, name])
		return result

	partner_id = fields.Many2one('res.partner', 'Empresa', required=True)
	name_empresa = fields.Char(related = 'partner_id.name')
	codigo = fields.Char('Codigo de contrato', required=True)
	fecha_inicio = fields.Date('Fecha inicio', required=True)
	fecha_finalizacion = fields.Date('Fecha finalización', required=True)
	notas = fields.Text('Observación')
	state = fields.Selection([('activo', 'Activo'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], string='Estado')	