# import json
# import werkzeug
from odoo import http
from odoo.http import request


class MountainController(http.Controller):

    @http.route('/mountain', auth='public', type='http')
    def mountain_check(self):
        return "Mountain check check check"

    # @http.route('/mountain/<int:id>', auth='public', type='http')
    # def mountain_check(self, id):
    #     return "Mountain check check check %s" % str(id)

    # @http.route('/mountain', auth='public')
    # def mountain_check(self):
    #     return werkzeug.utils.redirect('https://www.google.com')

    # @http.route('/mountain', auth='public')
    # def mountain_check(self):
    #     return request.render("web.login")

    # @http.route('/mountain', auth='public', type='http')
    # def mountain_check(self):
    #     return json.dumps({
    #         "check": "check 123"
    #     })

    # @http.route('/mountain', auth='public', type='http')
    # def mountain_check(self):
    #     partner = request.env['res.partner'].sudo().create({
    #         'name' : 'Mountain'
    #     })
    #     return 'Partner has been created'
