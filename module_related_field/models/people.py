from odoo import models, fields, api


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name')
