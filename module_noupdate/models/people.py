from odoo import models, fields


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
