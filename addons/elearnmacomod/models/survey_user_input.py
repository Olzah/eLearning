# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging


from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class SurveyUserInput(models.Model):
    _inherit = "survey.user_input"

    employee_id = fields.Many2one("hr.employee")

    @api.model_create_multi
    def create(self, vals_list):

        result = super(SurveyUserInput, self).create(vals_list)
        employee = self.env['hr.employee'].search([("work_email", "=", result.email)])
        employee.survey_user_input_ids |= result
        return result
