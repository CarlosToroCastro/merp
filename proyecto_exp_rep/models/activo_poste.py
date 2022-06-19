# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ActivoPoste(models.Model):

	_name = 'ct.activo_poste'
	_description = 'Equipo electrico, seccionador,cuchillas, transformador, (resto de estructuras)'


	tipo_activo_id = fields.Many2one('ct.tipo_activo_electrico', string="Tipo Activo Eléctrico", required=True)
	code_tipo_activo = fields.Char(related='tipo_activo_id.code')
	name = fields.Char('Código', required=True)
	tarea = fields.Integer('Tarea')
	serie = fields.Char('Serie')
	placa = fields.Char('Placa')
	capacidad = fields.Char('Capacidad')
	notas = fields.Text('Observación')
	
	_sql_constraints = [
		('activo_electrico_name_uniq', 'unique(name)', 'Información Repetida'),
	]


class TipoAtivoElectrico(models.Model):

	_name = 'ct.tipo_activo_electrico'
	_description = 'Ingresan los tipos de equipos electricos utilizados en MT y BT' 

	
	name = fields.Char('Nombre', required=True)
	code = fields.Char('Codigo Interno', required=True) 	
	notas = fields.Text('Observación')

	_sql_constraints = [
		('tipo_activo_electrico_code_uniq', 'unique(code)', 'Información Repetida'),
		('tipo_activo_electrico_name_uniq', 'unique(name)', 'Información Repetida')
	]


	"""class (object):"""
	"""docstring for """
	"""def __init__(self, arg):
		super(, self).__init__()
		self.arg = arg"""
