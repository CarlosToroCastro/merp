# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TipoArchivo(models.Model):

	_name = 'ct.tipo_archvivo'
	_description = 'Documentos necesrios para la elavoracion del proyecto'
	

	code = fields.Char('Código interno', required=True)
	name = fields.Char('Tipo Archivo', required=True) 	
	

	