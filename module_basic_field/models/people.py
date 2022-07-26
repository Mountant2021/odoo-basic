from odoo import models, fields


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name', size=8, trim=True, translate=True)
    available = fields.Boolean(string='Available')
    height = fields.Float(string='Height', digits='test1')
    age = fields.Integer(string='Age')
    test_trim = fields.Char(string='Test Trim')