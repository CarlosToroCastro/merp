# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TipoEquipoElectrico(models.Model):

	_name = 'ct.tipo_equipo_electrico'
	_description = 'Ingresan los tipos de equipos electricos utilizados en MT y BT' 

	codigo = fields.Char('codigo Tipo de de equipo', required=True)
	name = fields.Char('nombre de equipo', required=True) 	
	notas = fields.Text('Observación')