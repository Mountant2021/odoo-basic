from odoo import models, fields


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name')

    def action_check(self):
        self.ensure_one()
        self.id = 10
