# coding: utf-8
import psycopg2.errors
from odoo.exceptions import UserError
from odoo.tests import common, tagged


# This test should only be executed after all modules have been installed.
@tagged('-at_install', 'post_install')
class TestSurveyModel(common.TransactionCase):
    def test_calculate_rating(self):
        current_survey = self.env['survey.survey'].browse(5)
        self.assertEqual(current_survey.success_rating_count, 0)
        test_ratings = [
            {
                'reviewer_id': 1,
                'user_rating': '1',
                'survey_survey_id': current_survey.id,
                'opinion': "Some Example text"
            },
            {
                'reviewer_id': 2,
                'user_rating': '2',
                'survey_survey_id': current_survey.id,
                'opinion': "Some Example text"
            },
            {
                'reviewer_id': 3,
                'user_rating': '3',
                'survey_survey_id': current_survey.id,
                'opinion': "Some Example text"
            },
            {
                'reviewer_id': 4,
                'user_rating': '4',
                'survey_survey_id': current_survey.id,
                'opinion': "Some Example text"
            },
        ]
        for rating in test_ratings:
            self.assertTrue(self.env['survey.ratings'].create(rating))
        self.assertEqual(current_survey.success_rating_count, 2.5)

    def test_create_survey_rating(self):
        current_survey = self.env['survey.survey'].browse(5)
        set_rating = {
            'reviewer_id': 3,
            'user_rating': '3',
            'survey_survey_id': current_survey.id,
            'opinion': "Some Example text"
        }
        survey = self.env['survey.ratings'].create(set_rating)
        self.assertTrue(survey)

    def test_rate_survey_multiple_times(self):
        current_survey = self.env['survey.survey'].browse(5)
        set_rating = {
            'reviewer_id': 3,
            'user_rating': '3',
            'survey_survey_id': current_survey.id,
            'opinion': "Some Example text"
        }
        rating_1 = self.env['survey.ratings'].create(set_rating)
        self.assertTrue(rating_1)
        with self.assertRaises(psycopg2.errors.UniqueViolation):
            rating_2 = self.env['survey.ratings'].create(set_rating)

    def test_is_user_create_survey_rating_without_complete_survey(self):
        current_survey = self.env['survey.survey'].browse(5)
        set_rating = {
            'reviewer_id': 13,
            'user_rating': '3',
            'survey_survey_id': current_survey.id,
            'opinion': "Some Example text"
        }
        with self.assertRaises(UserError):
            survey = self.env['survey.ratings'].create(set_rating)

    def test_create_survey_rating_without_rate(self):
        current_survey = self.env['survey.survey'].browse(5)
        set_rating = {
            'reviewer_id': 13,
            'survey_survey_id': current_survey.id,
            'opinion': "Some Example text"
        }
        survey = self.env['survey.ratings'].create(set_rating)
        self.assertFalse(survey)
