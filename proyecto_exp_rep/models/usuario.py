# -*- coding: utf-8 -*-

from odoo import api, fields, models



class TMedidor(models.Model):

	_name = 'ct.tip_med'
	_description='Tipos de medidor mas utilizados'

	code_inte = fields.Char('código interno', required=True)
	name = fields.Char('Tipo de medidor', required=True)

	
class MarcaMedi(models.Model):

	_name = 'ct.marca_med'
	_description='Marcas de medidor'



	code_inte = fields.Char('código interno', required=True)
	name = fields.Char('Marca de medidor', required=True)




class Medidor(models.Model):

	_name = 'ct.medidor'
	_description = 'Caracteristicas del medidor'

	name = fields.Char('Serie', required=True)
	marca_id = fields.Many2one('ct.marca_med',string ='Marca de medidor', required=True)
	Tipo_Med_id = fields.Many2one('ct.tip_med',string ='Tipo de medidor', required=True)




class Usuario(models.Model):

	_name = 'ct.usuario'
	_description = 'Caracteristicas de los usuarios' #ATC, PQR, Inversión, RP
	 

	name = fields.Char('Código NIU', required=True)
	addres = fields.Char('Dirección', required=True)
	notas = fields.Text('Observación')
	medidor_id = fields.Many2one('ct.medidor', string='Medidor', required=True)
	nodo_id = fields.Many2one('ct.nodo', 'name', required=True)