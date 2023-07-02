from odoo import api, fields, models


class SurveySurvey(models.Model):
    _inherit = "survey.survey"

    success_rating_count = fields.Float("Success", compute="_compute_survey_rating_statistic")

    def _compute_survey_rating_statistic(self):
        self.success_rating_count = 0
        rating_records = self.env['survey.ratings'].search([("survey_survey_id", "=", self.id)])
        if rating_records:
            for rec in rating_records:
                self.success_rating_count += int(rec.user_rating)
            self.success_rating_count = round(self.success_rating_count / len(rating_records), 1)

    def action_set_ratings_2(self):
        action = self.env['ir.actions.act_window']._for_xml_id('elearnmacomod.survey_ratings_base_menu_action')
        ctx = dict(self.env.context)
        ctx.update({'search_default_survey_survey_id': self.id})
        action['context'] = ctx
        return action
