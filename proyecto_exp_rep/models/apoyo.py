# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Apoyo(models.Model):

	_name = 'ct.Apoyo'
	_description = 'Apoyo' 

	nodo_inicial = fields.Char('Nodo Inicial', required=True)
	nodo_Final = fields.Char('Nodo Final', required=True)
	#GPS
	#LISTA DE MANO DE OBRA
	#LISTA DE MATERIAL NUEVO
	#LISTA DE MATERIAL RETIRADO
	#LISTA DE MATERIAL REUTILIZADO
	#CARGAR O TOMAR FOTOS
	#LISTA DE ELEMENTOS CON CODIGO (TRANSFORMADOR, SECCIONADOR, CUCHILLAS,RCONECTADOR)
	notas = fields.Text('Observación')