# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    survey_user_input_ids = fields.One2many("survey.user_input", "employee_id", string='Survey Resume')



