from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char('Name', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    user_id = fields.Many2one('res.users', string='Responsible Person')
    description = fields.Text('Description')
    color = fields.Char('Color Index')
