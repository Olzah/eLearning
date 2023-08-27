# -*- coding: utf-8 -*-
{
    'name': 'mod_elearning',
    'author': "Oleh Zahorulko",
    'website': "http://www.example.com",
    'category': 'Services',
    'version': '0.0.1',
    'depends': ['base', 'hr', 'website_slides', 'survey'],
    'data': ['security/ir.model.access.csv', 'views/views.xml', 'views/hr_employee_view.xml', 'wizard/survey_ratings_wizard.xml',
             'views/survey_survey_views.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}