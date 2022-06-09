# -*- coding: utf-8 -*-
{
	'name': 'Expansión y Reposición',
	'version': '0.0.2',
	'author': 'Carlos Julio Toro Castro',
	'summary': 'Gestión de Proyectos en Sector Electrico',
	'depends': ['base_address_city', 'product','contacts'],
	'data': [
		'security/ir.model.access.csv',				
		'views/menu.xml',
		'views/product_template_views.xml',
		'views/tipo_proyecto_view.xml',
		'views/nivel_tension_view.xml',
		'views/subestacion_views.xml',
		'views/circuito_views.xml',
		'views/estructura_views.xml',
		'views/contrato_views.xml',
		'views/tipo_equpo_electrico_views.xml',
		'views/equipo_electrico_views.xml',
		'views/proyecto_views.xml',
	],
	'installable': True,
}