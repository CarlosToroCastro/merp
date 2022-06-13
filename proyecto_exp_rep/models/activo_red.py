# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ActivoRed(models.Model):

	_name = 'ct.activo_red'
	_description = 'Activos que corresponden a tramo de red'

	tipo_cable_ids = fields.One2many('ct.tipo_cable','activo_red_id',string="Red" )
	name = fields.Text('Nombre', required=True)
	name2 = fields.Text('Tarea', required=True)
	can_lineas = fields.Integer('Cantidad de lineas',required=True)
	distancia = fields.Float('Distancia entre nodos',required=True)




class TipoCable(models.Model):

	_name = 'ct.tipo_cable'
	_decription = 'Tipos de cable utilizadas para baja y media tensión'

	activo_red_id = fields.Many2one('ct.activo_red', 'name')
	name = fields.Char('Descripción corta del tipo de cable',required=True) 
	description = fields.Text('Descripcion completa del tipo de cable',required=True)	
	notas = fields.Text('Observación')
