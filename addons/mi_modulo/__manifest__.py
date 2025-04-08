# -*- coding: utf-8 -*-
{
    'name': "Mi Módulo",
    'summary': """
        Módulo de ejemplo para desarrollo en Odoo
    """,
    'description': """
        Este es un módulo de ejemplo para aprender a desarrollar en Odoo.
        Incluye modelos básicos y vistas para entender el proceso de desarrollo.
    """,
    'author': "Tu Nombre",
    'website': "https://www.ejemplo.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
} 