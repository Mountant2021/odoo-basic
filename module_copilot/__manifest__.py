{
    'name': 'Module Copilot',
    'summary': 'Module Copilot',
    'description': 'Module Copilot',
    'author': 'Odoo SA',
    'website': 'https://www.odoo.com',
    'category': 'Hidden',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/copilot_views.xml',
    ],
    'demo': [
        'data/copilot_demo.xml',
    ],
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'module_copilot/static/src/scss/module_copilot.scss',
            'module_copilot/static/src/js/module_copilot.js',
        ],
    },
}