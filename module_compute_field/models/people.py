from odoo import models, fields, api


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name')
    yob = fields.Integer(string='Year of Birth')
    cy = fields.Integer(string='Current Year')
    age = fields.Integer(string='Age', compute='_compute_age', store=True, inverse='_set_yob_cy')

    @api.depends('yob', 'cy')
    def _compute_age(self):
        for r in self:
            r.age = r.cy - r.yob

    def _set_yob_cy(self):
        for r in self:
            r.yob = 1

    def action_check_compute(self):
        self.ensure_one()
        self.name = 'Check 1'
