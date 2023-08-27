from odoo import api, fields, models


class SurveyRatings(models.Model):
    _name = "survey.ratings"
    _description = "Survey Rating"

    _sql_constraints = [
        ('reviewer_rate_uniq', 'unique(survey_survey_id, reviewer_id)',
         "SQL Vadidation Error! 'Sorry, You cannot rate this Survey more than once!"),
    ]

    reviewer_id = fields.Many2one('hr.employee', string='Reviewer')
    rating = fields.Float('Survey Rating', compute="_compute_survey_rating")
    user_rating = fields.Selection([('1', 'Label 1'), ('2', 'Label 2'), ('3', 'Label 3'), ('4', 'Label 4'), ('5', 'Label 5')], string='Set Rating', required=True)
    survey_survey_id = fields.Many2one("survey.survey", string="Survey", index=True)
    opinion = fields.Char(string='Comment', required=True)
    success_rating_count = fields.Integer("Success", compute="_compute_survey_rating_statistic")

    @api.depends('user_rating')
    def _compute_survey_rating(self):
        pass

    def _compute_survey_rating_statistic(self):
        self.success_rating_count = 0
        print("cos tutaj: ", self.success_rating_count)
        rating_records = self.env['survey.rating'].search(["survey_survey_id", "=", self.survey_survey_id.id])
        for rec in rating_records:
            self.success_rating_count += rec.get("user_rating")
        print(round(self.success_rating_count/len(rating_records), 1))
        return round(self.success_rating_count/len(rating_records), 1)

