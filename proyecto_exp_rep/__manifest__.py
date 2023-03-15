# -*- coding: utf-8 -*-
{
	'name': 'Expansión y Reposición',
	'version': '0.0.2',
	'author': 'Carlos Julio Toro Castro',
	'summary': 'Gestión de Proyectos en Sector Electrico',
	'depends': ['base_address_extended', 'product','contacts','stock'],
	'data': [
		'security/merp_security.xml',
		'security/ir.model.access.csv',
		'data/mail_template_data.xml',				
		'views/menu.xml',
		'views/product_template_views.xml',
		'views/rol_views.xml',
		'views/nivel_tension_views.xml',
		'views/subestacion_views.xml',
		'views/circuito_views.xml',
		'views/estructura_views.xml',
		'views/contrato_views.xml',
		'views/tipo_activo_electrico_views.xml',
		'views/tipo_proyecto_views.xml',
		'views/nodo_views.xml',
		'views/nodo_image_views.xml',		
		'views/seguimiento_control_views.xml',
		'views/proyecto_views.xml',
		'views/tipo_medidor_views.xml',
		'views/marca_medidor_views.xml',
		'views/medidor_views.xml',
		'views/usuario_views.xml',
		'views/activo_nodo_views.xml',
		'views/tipo_luminaria_views.xml',
		'views/pot_luminaria_views.xml',
		'views/luminaria_views.xml',
		'views/pot_trans_views.xml',
		'views/anexos_views.xml',
		'views/no_conformidades_views.xml',	
		'views/fases_views.xml',
		'views/actividades_views.xml',
		
		
	],
	'installable': True,
	'assets': {
        'web.assets_backend': [
            'proyecto_exp_rep/static/src/scss/nodo_image_kanban.scss',
        ],	
	},	

}