from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    people_id = fields.Many2one('people', string='People')
    name = fields.Char(related='people_id.name', store=True)
