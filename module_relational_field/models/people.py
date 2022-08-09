from odoo import models, fields


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name')

    # One2many field
    house_ids = fields.One2many('house', 'people_id', string='House')
