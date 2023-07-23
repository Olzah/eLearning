# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class RateSurveyWizard(models.TransientModel):
    _name = 'rate.survey.wizard'
    _description = 'Rate survey Wizard'

    def _get_employee_id(self):
        employee_rec = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        return employee_rec.id

    def _get_active_rec_id(self):
        return self.env.context.get('active_id')

    reviewer_id = fields.Many2one('hr.employee', string='Reviewer', default=_get_employee_id)
    survey_ids = fields.Many2one('survey.survey', string='Survey', default=_get_active_rec_id)
    opinion = fields.Char(string='Comment', required=True)
    user_rating = fields.Selection(
        [('1', 'Label 1'), ('2', 'Label 2'), ('3', 'Label 3'), ('4', 'Label 4'), ('5', 'Label 5')], string='Set Rating')

    def add_survey_ratings(self):
        current_survey = self.env['survey.survey'].search([('id', '=', self.survey_ids.id)])

        count_review = current_survey.user_input_ids.filtered(lambda record: record.partner_id.id == self.reviewer_id.id and record.state == 'done')
        if len(count_review) > 0:
            raise UserError('Sorry, You cant rate this Survey! You have to finish the course first!')

        self.env['survey.ratings'].create({
                        'reviewer_id': self.reviewer_id.id,
                        'survey_survey_id': self.survey_ids.id,
                        'opinion': self.opinion,
                        'user_rating': self.user_rating,
                    })

