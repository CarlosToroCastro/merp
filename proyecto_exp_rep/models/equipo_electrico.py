# -*- coding: utf-8 -*-

from odoo import api, fields, models

class EquipoElectrico(models.Model):

	_name = 'ct.equipo_electrico'
	_description = 'Equipo electrico, seccionador,cuchillas, transformador'


	tipo_equipo_id = fields.Many2one('ct.tipo_equipo_electrico', string="Tipo equipo electrico")
	direccion = fields.Char('Dirección', required=True)
	codigo = fields.Char('Codigo', required=True)
	serie = fields.Char('Serie')
	nodo = fields.Char('Nodo')
	capacidad = fields.Char('Capacidad')
	notas = fields.Text('Observación')
	state = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutililizado'), ('Retirado', 'Retirado')], string='Estado')
	