{
    'name': 'Module Owl',
    'summary': 'Module Owl',
    'description': 'Module Owl',
    'author': 'Odoo SA',
    'website': 'https://www.odoo.com',
    'category': 'Hidden',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'module_owl/static/src/components/*/*.js',
            'module_owl/static/src/components/*/*.xml',
        ],
    },
    'installable': True,
}