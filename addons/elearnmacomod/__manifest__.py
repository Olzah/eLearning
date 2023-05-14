# -*- coding: utf-8 -*-
{
    'name': 'mod_elearning',
    'author': "Oleh Zahorulko",
    'website': "http://www.example.com",
    'category': 'Services',
    'version': '0.0.1',
    'depends': ['base', 'hr', 'website_slides'],
    'data': ['security/ir.model.access.csv', 'views/views.xml', 'views/hr_employee_view.xml',
             'views/survey_survey_views.xml', 'wizard/survey_ratings_wizard.xml'],
    'demo': ['demo.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}