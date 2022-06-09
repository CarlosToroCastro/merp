# -*- coding: utf-8 -*-

from odoo import api, fields, models

class NivelTension(models.Model):

	_name = 'ct.nivel_tension'
	_description = 'Nivel de Tensión' #ATC, PQR, Inversión, RP 

	
	name = fields.Char('Nivel de Tensión', required=True) #ATC, PQR, Inversión, RP 	
	notas = fields.Text('Observación')