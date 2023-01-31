from odoo import models, fields


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='draft')
    parent_id = fields.Many2one('people', string='Parent')
    parent_path = fields.Char(index=True)
    company = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
