# coding: utf-8
from odoo.tests import common, tagged


# This test should only be executed after all modules have been installed.
@tagged('-at_install', 'post_install')
class TestSurveyModel(common.TransactionCase):
    def test_calculate_rating(self):
        current_survey = self.env['survey.survey'].browse(5)
        current_survey._compute_survey_rating_statistic()
        current_survey.success_rating_count
        self.assertEqual(current_survey.success_rating_count, 2.3)

    def test_create_survey_rating(self):
        current_survey = self.env['survey.survey'].browse(5)
        set_rating = {
            'reviewer_id': 3,
            'user_rating': 12,
            'survey_survey_id': current_survey.id,
            'opinion': "Some Example text"
        }
        survey = self.env['survey.survey'].create(set_rating)
        self.assertTrue(survey)

    def test_is_user_create_survey_rating_without_complete_survey(self):
        current_survey = self.env['survey.survey'].browse(5)
        set_rating = {
            'reviewer_id': 13,
            'user_rating': 12,
            'survey_survey_id': current_survey.id,
            'opinion': "Some Example text"
        }
        survey = self.env['survey.survey'].create(set_rating)
        self.assertTrue(survey)

    def test_create_survey_rating_without_rate(self):
        current_survey = self.env['survey.survey'].browse(5)
        set_rating = {
            'reviewer_id': 13,
            'survey_survey_id': current_survey.id,
            'opinion': "Some Example text"
        }
        survey = self.env['survey.survey'].create(set_rating)
        self.assertTrue(survey)
