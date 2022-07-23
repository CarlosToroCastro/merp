# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ArchivoProyecto(models.Model):

	_name = 'ct.archivo_proyecto'
	_description = ''
	

	tipo_archivo_id = fields.Many2one('ct.tipo_archvivo', string='Tipo')
	proyecto_id = fields.Many2one('ct.proyecto',string='proyecto')
	filename = fields.Char('Nombre Archivo')
	anexo = fields.Binary('Archivo')
	notas = fields.Text('Observaciones') 	
	