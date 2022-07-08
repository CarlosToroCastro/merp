# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Nodo(models.Model):

	_name = 'ct.nodo'
	_description = 'Poste, camara de inspeción u otro tipo de nodo' 


	name = fields.Char('Nodo', required=True)
	gps_altura = fields.Float('Altitud m.s.n.m')
	gps_latitud = fields.Float('Latitud')
	gps_longitud =fields.Float('Longitud')
	direccion = fields.Char('Dirección', required=True)
	notas = fields.Text('Observación')
	activo_poste_ids = fields.One2many('ct.nodo_activo','nodo1_id', string="Activos")
	luminaria_ids = fields.One2many('ct.luminaria','nodo_id', string="Luminaria")
	usuario_ids = fields.One2many('ct.usuario','nodo_id', string="Usuario")
	proyecto_id = fields.Many2one('ct.proyecto', 'name')
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')

	def btn_replanteo(self):
		self.state = 'replanteo'

		lineas_replanteo =[]
		for activo in self.activo_poste_ids:
			nueva_linea = {
					'nodo1_id': activo.nodo1_id.id,
					'a_poste_id': activo.a_poste_id.id,
					'state1': activo.state1,
					'tarea': activo.tarea,
					'notes': activo.tarea,
					#pasar los product tambien
					'state': 'replanteo' 
			}
			lineas_replanteo.append((0,0, nueva_linea))

			if lineas_replanteo:
				self.activo_poste_ids = lineas_replanteo


class ActivoPosteNodo(models.Model):
#realacion  entre activos y nodos. 
	_name = 'ct.nodo_activo'
	_description = 'Activos que se encuentran en un nodo'


	nodo1_id = fields.Many2one('ct.nodo', 'name', required=True)
	a_poste_id = fields.Many2one('ct.activo_poste', 'Activo',  required=True)
	tipo_activo_id = fields.Many2one(related='a_poste_id.tipo_activo_id')
	state1 = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutilizado'), ('Retirado', 'Retirado')], string='Estado', required=True)
	tarea = fields.Integer('Tarea MAXIMO', required=True)
	notes = fields.Text('Observación')
	product_ids = fields.One2many('ct.product_activo', 'activo_nodo_id', required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')


class productActivo(models.Model):
	#cantidad de mano de obra que se puede realizar en un activo.

	_name = 'ct.product_activo' 
	_description = 'Mano de obra y materiales que se utilizada en un activo'


	activo_nodo_id = fields.Many2one('ct.nodo_activo', 'Activo', required=True)
	product_id = fields.Many2one('product.template',string='Producto', required=True)
	cantidad = fields.Float('Cantidad', required=True)
	tipo_product = fields.Selection([('mo', 'MO'), ('nuevo', 'Nuevo'), ('retirado', 'Retirado'),('reutilizado','Reutilizado')], required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')




###NO SIRVE PARA NADA PERO NO SE PUEDE QUITAR
class productActivo2(models.Model):
	#cantidad de mano de obra que se puede realizar en un activo.

	_name = 'product_activo' 
	_description = 'Mano de obra y materiales que se utilizada en un activo'

	cantidad = fields.Float('Cantidad', required=True)
	
###NO SIRVE PARA NADA PERO NO SE PUEDE QUITAR
class ActivoPosteNodo2(models.Model):
#realacion  entre activos y nodos. 
	_name = 'ct.nodo.activo_poste'
	_description = 'Activos que se encuentran en un nodo'

	cantidad = fields.Float('Cantidad', required=True)