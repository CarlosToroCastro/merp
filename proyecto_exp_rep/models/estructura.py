# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Estructura(models.Model):

	_name = 'ct.estructura'
	_description = 'Estructura'

     
	name = fields.Char('Código de la estructura',required=True)
	descripcion = fields.Text('Descripción', required=True)
	familia = fields.Char('Familia', required=True) #centro, bandera, semibandera, H....
	tipo = fields.Selection([('retencion', 'Retención'), ('suspension', 'Suspensión')], string='Tipo Estructura',required=True)
	nivel_tension_id = fields.Many2many('ct.nivel_tension', string='Nivel tensión', required=True)
	materiales_ids = fields.One2many('ct.materiales_estructura', 'estructura_id', string="Material de la estructura")
	
	
	

class MaterialesEstructura(models.Model):

	_name = 'ct.materiales_estructura'
	_description = 'Matariales empleados en la estructura'

	estructura_id = fields.Many2one('ct.estructura', 'name',required=True)
	product_id = fields.Many2one('product.template', 'Material',required=True)
	cantidad = fields.Float('Cantidad',required=True)

	
	#stage_id