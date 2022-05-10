from odoo import http
from odoo.addons.module_controller.controllers.main import MountainController


class MountainController(MountainController):

    @http.route('/mountain')
    def mountain_check(self):
        super(MountainController, self).mountain_check()
        return "inherit"