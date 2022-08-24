from odoo import models, fields


class People(models.Model):
    _name = 'people'
    _description = 'People'

    def _selection_list(self):
        return [(model.model, model.name) for model in self.env['ir.model'].search([])]

    name = fields.Char(string='Name')

    # Reference field
    reference = fields.Reference(selection=_selection_list, string='Reference')

    # Many2oneReference field
    res_model = fields.Char('Model Name', required=True, index=True)
    m2o_reference = fields.Many2oneReference(model_field='res_model', string='Many2oneReference')
