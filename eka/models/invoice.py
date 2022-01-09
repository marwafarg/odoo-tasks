from odoo import api, fields, models

class Cyber_account_move(models.Model):
    _inherit = 'account.move'

    start_work_date = fields.Date(string="Start Working Date", required=False, )
    end_work_date = fields.Date(string="End Working Date", required=False, )