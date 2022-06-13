# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Nodo(models.Model):

	_name = 'ct.nodo'
	_description = 'Poste, camara de inspeción u otro tipo de nodo' 


	name2 = fields.Char('Nodo Inicial', required=True)
	name = fields.Char('Nodo Final', required=True)
	gps_latitud = fields.Float('latitud')
	gps_longitud =fields.Float('longitud')
	gps_altura = fields.Float('altura')
	direccion = fields.Char('Dirección', required=True)
	notas = fields.Text('Observación')






	#GPS
	#LISTA DE MANO DE OBRA
	#LISTA DE MATERIAL NUEVO
	#LISTA DE MATERIAL RETIRADO
	#LISTA DE MATERIAL REUTILIZADO
	#LISTA DE PENDIENTES
	#CARGAR O TOMAR FOTOS
	#LISTA DE ELEMENTOS CON CODIGO (TRANSFORMADOR, SECCIONADOR, CUCHILLAS,RCONECTADOR)
	