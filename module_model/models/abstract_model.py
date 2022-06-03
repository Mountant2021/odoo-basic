from odoo import models, fields


class AnimalAbstract(models.AbstractModel):
    _name = 'animal.abstract'
    _description = 'Animal Abstract'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], string='Gender')
    color = fields.Char(string='Color')
    age = fields.Integer(string='Age')

    def _sound(self):
        pass
