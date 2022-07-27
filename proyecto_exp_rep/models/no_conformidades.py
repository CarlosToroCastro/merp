# -*- coding: utf-8 -*-

from odoo import api, fields, models

class NoConformidades(models.Model):

	_name = 'ct.no_conformidades'
	_description = 'Irregularidades encontradas en cada nodo'
	

	code = fields.Char('Código', required=True)
	name = fields.Char('No conformidad', required=True) 	
	

	