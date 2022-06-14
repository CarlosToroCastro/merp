# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ActivoPoste(models.Model):

	_name = 'ct.activo_poste'
	_description = 'Equipo electrico, seccionador,cuchillas, transformador, (resto de estructuras)'


	nodo_id = fields.Many2one('ct.nodo','name')
	tipo_activo_id = fields.Many2one('ct.tipo_activo_electrico', string="Tipo Activo Eléctrico")
	code_tipo_activo = fields.Char(related='tipo_activo_id.code')
	name = fields.Char('Código', required=True)
	tarea = fields.Integer('Tarea')
	serie = fields.Char('Serie')
	placa = fields.Char('Placa')
	capacidad = fields.Char('Capacidad')
	notas = fields.Text('Observación')
	state = fields.Selection([('nuevo', 'Nuevo'), ('reutilizado', 'Reutililizado'), ('Retirado', 'Retirado')], string='Estado')
	