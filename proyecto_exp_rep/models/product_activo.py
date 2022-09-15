# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class productActivo(models.Model):
	#cantidad de mano de obra que se puede realizar en un activo.

	_name = 'ct.product_activo' 
	_description = 'Mano de obra y materiales que se utilizada en un activo'


	activo_nodo_id = fields.Many2one('ct.activo_nodo', 'Activo')
	nodo_id = fields.Many2one(related='activo_nodo_id.nodo_id', store=True, string = "Nodo")
	proyecto_id = fields.Many2one(related='activo_nodo_id.nodo_id.proyecto_id', store=True)
	tipo_activo_code = fields.Char(related='activo_nodo_id.tipo_activo_code')
	product_id = fields.Many2one('product.template',string='Producto')
	cat_product = fields.Many2one(related = 'product_id.categ_id', string = "Categoria")
	estructura_product_ids = fields.Many2many(related='product_id.estructura_ids')
	valor_uni = fields.Float('V Uni', default=0)
	valor_tot = fields.Float('V Total', default=0)
	distancia = fields.Integer('Dist', default=1)		
	can_lineas = fields.Selection([('1', 1), ('2', 2),('3', 3),('4', 4)], default = '1', string="Can lineas")
	cantidad = fields.Integer('Total', default = 1)
	estructura_ids = fields.Many2one('ct.estructura', string='Estructuras')
	vali_len_estruc = fields.Boolean(default=False)
	bodega=fields.Char('Bodega')
	tipo_product = fields.Selection([('mo', 'Mano de Obra'), ('nuevo', 'Nuevo'), ('retirado', 'Retirado'),('reutilizado','Reutilizado')], required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], string='Etapa')

	"""@api.constrains("cantidad")
	def _constrain_cantidad(self):
		for record in self:
			if record.cantidad <= 0:
				raise ValidationError('Debe especificar una cantidad')
				"""

	 # Si la cantidad es 0 o un numero negativo se convierte en 1
	@api.onchange("can_lineas" , "distancia")
	def onchange_cantidad(self):
		self.cantidad = int(self.can_lineas) * self.distancia
		if self.cantidad <= 0:
			self.cantidad = 1
			return {
				"warning": {"title": "Error en Cantidad",	"message": "Debe especificar una cantidad mayor a cero" }
			}	

	#Indicar el tipo de producto y el estado. 
	@api.onchange("product_id")
	def onchange_valor_uni(self):
		_logger.info('Nueva linea %s', 'onchange_valor_uni')
		if self.product_id:
			self.state = self.activo_nodo_id.state 
			if self.product_id.detailed_type == 'service':
				self.tipo_product = 'mo'
			elif self.product_id.detailed_type == 'product':
				self.tipo_product = 'nuevo'
			elif self.product_id.name2 == 'Retirado':
				self.tipo_product = 'retirado'


	#Si la MO tiene estructuras se vuelve requerido, si tiene una sola estructura la pone por defecto.  
	@api.onchange("product_id")
	def onchange_estruc_required(self):
		self.estructura_ids = False
		if len(self.product_id.estructura_ids) != 0:
			self.vali_len_estruc = True 
			if len(self.product_id.estructura_ids) == 1: # Si solo hay una estructura queda por defecto. 
				self.estructura_ids = self.product_id.estructura_ids
		else: 
			self.vali_len_estruc = False

	#Obtener el valor unitario y total de mo y material nuevo. 
	@api.onchange("product_id", "cantidad" )
	def onchange_v_total(self):
		if self.product_id:
			self.valor_uni = self.product_id.list_price 
			self.valor_tot = self.valor_uni * self.cantidad
		
