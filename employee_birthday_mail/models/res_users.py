# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUsers(models.Model):

    _inherit = 'res.users'

    body_action = fields.Html(string='Body Action')
    report_header = fields.Html(string='Report Header')
    report_footer = fields.Html(string='Report Footer')
