from odoo import models, fields


class People(models.Model):
    _name = 'people'
    _description = 'People'

    name = fields.Char(string='Name')

    # Binary field
    cv1 = fields.Binary(string='CV 1')
    cv2 = fields.Binary(string='CV 2', attachment=False)

    # HTML field
    description = fields.Html(string='Description', sanitize_tags=False)
    description2 = fields.Html(string='Description 2', sanitize_tags=False)

    # Image field
    avatar = fields.Image(string='Avatar', max_width=1920, max_height=1920)

    # Selection field
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    # Text field
    information = fields.Text(string='Information')
