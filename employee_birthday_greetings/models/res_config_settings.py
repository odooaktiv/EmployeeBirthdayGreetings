# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    body_action = fields.Html(
        related='company_id.body_action', string='Body Action')
    report_header = fields.Html(
        related='company_id.report_header', string='Report Header')
    report_footer = fields.Html(
        related='company_id.report_footer', string='Report Footer')
