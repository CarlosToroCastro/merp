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
		'views/rol_views.xml',
		'views/nivel_tension_views.xml',
		'views/subestacion_views.xml',
		'views/circuito_views.xml',
		'views/estructura_views.xml',
		'views/contrato_views.xml',
		'views/tipo_activo_electrico_views.xml',
		'views/activo_poste_views.xml',
		'views/tipo_proyecto_views.xml',
		'views/nodo_views.xml',
		'views/seguimiento_control_views.xml',
		'views/proyecto_views.xml',
		'views/tipo_medidor_views.xml',
		'views/marca_medidor_views.xml',
		'views/medidor_views.xml',
		'views/usuario_views.xml',
		'views/activo_x_nodo_views.xml',
		
	],
	'installable': True,
}