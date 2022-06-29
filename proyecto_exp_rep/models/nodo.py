# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Nodo(models.Model):

	_name = 'ct.nodo'
	_description = 'Poste, camara de inspeción u otro tipo de nodo' 


	name = fields.Char('Nodo', required=True)
	gps_altura = fields.Float('Altura')
	gps_latitud = fields.Float('Latitud')
	gps_longitud =fields.Float('Longitud')
	direccion = fields.Char('Dirección', required=True)
	notas = fields.Text('Observación')
	activo_poste_ids = fields.One2many('ct.nodo.activo_poste','nodo1_id', string="Activos")
	proyecto_id = fields.Many2one('ct.proyecto', 'name', required=True)
	#state = fields.Selection([('diseño', 'Diseño'), ('replanteo', 'Replanteo'), ('ejecucion', 'Ejecución')], default='diseño')



class ActivoPosteNodo(models.Model):
#realcion  entre activos y nodos. 
	_name = 'ct.nodo.activo_poste'
	_description = 'Activos que se encuentran en un nodo'


	nodo1_id = fields.Many2one('ct.nodo', 'name', required=True)
	a_poste_id = fields.Many2one('ct.activo_poste', 'Activo',  required=True)
	tipo_activo_id = fields.Many2one(related='a_poste_id.tipo_activo_id')
	state = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutililizado'), ('Retirado', 'Retirado')], string='Estado', required=True)
	tarea = fields.Integer('Tarea', required=True)
	notes = fields.Text('Observación')
	m_obra_ids = fields.One2many('ct.m.obra_a.poste','a_poste_id',required=True)


class MObraActivo(models.Model):
	#cantidad de mano de obra que se puede realizar en un activo.

	_name = 'ct.m.obra_a.poste' 
	_description = 'Mano de obra utilizada en un activo'


	a_poste_id = fields.Many2one('ct.nodo.activo_poste', 'Activo', required=True)
	product_id = fields.Many2one('product.template', 'Mano de obra', required=True)
	cantidad = fields.Float('Cantidad', required=True)