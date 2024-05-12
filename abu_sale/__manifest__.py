# -*- coding: utf-8 -*-
{
    'name': "ABU Integrated ERP Systems (AIES)",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Andromeda",
    'website': "https://andromedasupendi.pythonanywhere.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','web','sale','purchase','board','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/kwitansi_template.xml',
        'views/abu_dashboard.xml',
        'views/kwitansi_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'abu_sale/static/src/components/**/*.js',
            'abu_sale/static/src/components/**/*.xml',
            'abu_sale/static/src/components/**/*.scss',
        ],
    },
}
