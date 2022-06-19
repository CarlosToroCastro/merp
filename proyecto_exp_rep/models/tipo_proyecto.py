# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TipoProyecto(models.Model):

	_name = 'ct.tipo_proyecto'
	_description = 'Tipo de proyectop' #ATC, PQR, Inversión, RP
	_rec_name = 'tipo_proyecto' 

	code = fields.Char('Código interno')
	tipo_proyecto = fields.Char('Tipo Proyecto', required=True) #ATC, PQR, Inversión, RP 	
	notas = fields.Text('Observación')

	_sql_constraints = [
		('tipo_proyect_code_uniq', 'unique(code)', 'Informacion Repetida'),
		('tipo_proyecto_name_uniq', 'unique(tipo_proyecto)', 'Informacion Repetida'),
	]