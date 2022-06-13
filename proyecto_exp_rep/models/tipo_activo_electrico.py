# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TipoAtivoElectrico(models.Model):

	_name = 'ct.tipo_activo_electrico'
	_description = 'Ingresan los tipos de equipos electricos utilizados en MT y BT' 

	
	name = fields.Char('Nombre',required=True) 	
	notas = fields.Text('Observación')
