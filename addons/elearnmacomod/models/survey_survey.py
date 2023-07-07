from odoo import api, fields, models


class SurveySurvey(models.Model):
    _inherit = "survey.survey"

    success_rating_count = fields.Integer("Success", compute="_compute_survey_rating_statistic")

    def _compute_survey_rating_statistic(self):
        self.success_rating_count = 0
        rating_records = self.env['survey.ratings'].search([("survey_survey_id", "=", self.id)])
        for rec in rating_records:
            self.success_rating_count += int(rec.user_rating)
        return round(self.success_rating_count / len(rating_records), 1)
    def action_set_ratings_2(self):
        print('Hello World from survey.survey!!!')
