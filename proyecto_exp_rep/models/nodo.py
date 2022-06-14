# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Nodo(models.Model):

	_name = 'ct.nodo'
	_description = 'Poste, camara de inspeción u otro tipo de nodo' 


	#name2 = fields.Char('Nodo Inicial', required=True)
	name = fields.Char('Nodo', required=True)
	gps_latitud = fields.Float('Latitud')
	gps_longitud =fields.Float('Longitud')
	gps_altura = fields.Float('Altura')
	direccion = fields.Char('Dirección', required=True)
	notas = fields.Text('Observación')
	activo_poste_ids = fields.One2many('ct.activo_poste','nodo_id', string="Activos")
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')

	mano_obra_ids = fields.One2many('ct.nodo.mano_obra', 'nodo_id', 'Mano de Obra')


	def btn_replanteo(self):
		self.state = 'replanteo'

		lineas_replanteo = []
		for mobra in self.mano_obra_ids:
			nueva_linea = {
				'nodo_id': mobra.nodo_id.id,
				'product_id': mobra.product_id.id,
				'cantidad': mobra.cantidad,
				'state': 'replanteo'
			}
			lineas_replanteo.append((0, 0, nueva_linea))

		if lineas_replanteo:
			self.mano_obra_ids = lineas_replanteo






class ManoObraNodo(models.Model):

	_name = 'ct.nodo.mano_obra'
	_description = 'Mano de Obra Nodo'

	nodo_id = fields.Many2one('ct.nodo', 'Nodo', required=True)
	state_nodo = fields.Selection(related='nodo_id.state')
	product_id = fields.Many2one('product.template', 'Elemento', required=True)
	cantidad = fields.Float('Cantidad', required=True)
	state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')


	#GPS
	#LISTA DE MANO DE OBRA
	#LISTA DE MATERIAL NUEVO
	#LISTA DE MATERIAL RETIRADO
	#LISTA DE MATERIAL REUTILIZADO
	#LISTA DE PENDIENTES
	#CARGAR O TOMAR FOTOS
	#LISTA DE ELEMENTOS CON CODIGO (TRANSFORMADOR, SECCIONADOR, CUCHILLAS,RCONECTADOR)
	