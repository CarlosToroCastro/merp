# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Luminaria(models.Model):

	_name = 'ct.luminaria'
	_description = 'Difrentres tipos de luminaria existentes'

	tipo_lumi_id=fields.Many2one('ct.tipo_lumi','Tipo', required=True)
	pot_lumi_id=fields.Many2one('ct.pot_lumi', 'Potencia', required=True)
	cantidad=fields.Integer('Cantidad', required=True)
	nodo_id = fields.Many2one('ct.nodo', 'name', required=True)	

class TipoLumi(models.Model):

	_name = 'ct.tipo_lumi'
	_description = 'Tipos de luminarias mas conocidos'

	code = fields.Char('Codigo Interno', required=True)
	name = fields.Char('Tipo de Luminaria', required=True)

class PoLumi(models.Model):

	_name = 'ct.pot_lumi'
	_description = 'Tipos de luminarias mas conocidos'

	code = fields.Char('Codigo Interno', required=True)
	name = fields.Char('Potencia Luminaria', required=True)