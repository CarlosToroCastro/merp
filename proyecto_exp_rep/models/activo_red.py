# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ActivoRed(models.Model):

	_name = 'ct.activo_red'
	_description = 'Activos que corresponden a tramo de red'

	tipo_cable_ids = fields.One2many('ct.tipo_cable','activo_red_id',string="Red" )
	name = fields.Char('Nodo Inicial',required=True)
	name2 = fields.Char('Nodo Final', required=True)
	tarea = fields.Text('Tarea', required=True)
	distancia = fields.Float('Distancia entre nodos',required=True)
	nivel_tension_id = fields.Many2one('ct.nivel_tension', string='Nivel Tensión',required=True)
	des_red_ids = fields.One2many('ct.des_red','activo_red_id')
	

class desRed(models.Model):

	_name = 'ct.des_red'
	_description = 'Activos que corresponden a tramo de red'

	activo_red_id = fields.Many2one('ct.activo_red', 'name')
	tipo_cable_id = fields.Many2one()
	can_lineas = fields.Integer('Cantidad de lineas',required=True)
	accion = fields.Selection([('instalar', 'Instalar'), ('retirar', 'Retirar'),('retemplar', 'Retemplar') ], string='Acción')
	#total_red = """


class TipoCable(models.Model):

	_name = 'ct.tipo_cable'
	_decription = 'Tipos de cable utilizadas para baja y media tensión'

	
	name = fields.Char('Descripción corta del tipo de cable',required=True) # va en otra tabla
	description = fields.Text('Descripcion completa del tipo de cable',required=True)	
	notas = fields.Text('Observación')
	activo_red_id = fields.Many2one('ct.activo_red', 'name')
