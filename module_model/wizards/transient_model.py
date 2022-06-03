from odoo import models, fields


class TransientModel(models.TransientModel):
    _name = 'transient.model'
    _description = 'Transient Model'

    name = fields.Char(string='Name')

    def action_create_dog(self):
        for r in self:
            dog = self.env['dog'].create({'name': r.name})