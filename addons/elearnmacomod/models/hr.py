# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    test_field = fields.Char('Departmentss Namesss', required=True)