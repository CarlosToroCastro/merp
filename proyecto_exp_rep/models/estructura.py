# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Estructura(models.Model):

	_name = 'ct.estructura'
	_description = 'Estructura'

	def name_get(self):
		""" Personalizar nombre a mostrar en campos de seleccion"""
		result = []
		for record in self:
			name = "[%s] %s " % (record.name, record.descripcion)
			result.append([record.id, name])
		return result 

	name = fields.Char('Código de la estructura',required=True)
	descripcion = fields.Text('Descripción', required=True)
	familia = fields.Char('Familia') #centro, bandera, semibandera, H....
	tipo = fields.Selection([('retencion', 'Retención'), ('suspension', 'Suspensión')])
	nivel_tension_id = fields.Many2many('ct.nivel_tension', string='Nivel tensión', required=True)
	materiales_ids = fields.One2many('ct.materiales_estructura', 'estructura_id', string="Material de la estructura")
	product_activo_id = fields.One2many('ct.product_activo', 'estructura_ids')
	

	_sql_constraints = [
		('estructuras_uniq', 'unique(name)', 'Esta estructura ya existe'),
		
	]
	
	

class MaterialesEstructura(models.Model):

	_name = 'ct.materiales_estructura'
	_description = 'Matariales empleados en la estructura'

	estructura_id = fields.Many2one('ct.estructura', 'name',required=True)
	product_id = fields.Many2one('product.template', 'Material', required=True)
	cantidad = fields.Float('Cantidad',default=1, required=True)
	
    
	#@api.constrains("cantidad")
	#def _constrain_cantidad(self):
		#if self.cantidad <= 0:
			#raise ValidationError('Debe especificar una cantidad')

	 # Si la cantidad es 0 o un numero negativo se convierte en 1
	@api.onchange("cantidad")
	def onchange_cantidad(self):
		if self.cantidad <= 0:
			self.cantidad = 1
			return {
				"warning": {"title": "Error en Cantidad",	"message": "Debe especificar una cantidad mayor a cero" }
			}
	