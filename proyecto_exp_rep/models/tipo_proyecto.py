# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TipoProyecto(models.Model):

	_name = 'ct.tipo_proyecto'
	_description = 'Tipo de proyectop' #ATC, PQR, Inversión, RP
	_rec_name = 'tipo_proyecto' 

	tipo_proyecto = fields.Char('Tipo Proyecto', required=True) #ATC, PQR, Inversión, RP 	
	notas = fields.Text('Observación')