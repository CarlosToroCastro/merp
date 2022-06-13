# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ActivoPoste(models.Model):

	_name = 'ct.activo_poste'
	_description = 'Equipo electrico, seccionador,cuchillas, transformador, (resto de estructuras)'


	tipo_activo_id = fields.Many2one('ct.tipo_activo_electrico', string="Tipo activo electrico")
	codigo = fields.Char('Codigo', required=True)
	serie = fields.Char('Serie')
	nodo = fields.Char('Nodo - placa')
	capacidad = fields.Char('Capacidad')
	notas = fields.Text('Observación')
	state = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutililizado'), ('Retirado', 'Retirado')], string='Estado')
	