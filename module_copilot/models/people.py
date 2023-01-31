from odoo import fields, models, api

class People(models.Model):
    _name = 'module_copilot.people'
    _description = 'People'

    name = fields.Char(string='Name', required=True, tracking=True)
    yob = fields.Integer(string='Year of Birth', required=True, tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True, tracking=True)

    @api.depends('yob')
    def _compute_age(self):
        # compute age from year of birth, current year is 2022
        for record in self:
            record.age = 2022 - record.yob