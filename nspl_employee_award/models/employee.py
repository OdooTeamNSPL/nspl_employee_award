from odoo import models, fields, api


class AwardType(models.Model):
    _name = 'award.type'
    _description = 'Award Type'
    _rec_name = 'award_name'

    award_name = fields.Char(string='Name', required=True)


class EmployeeAwardForm(models.Model):
    _name = 'employee.award'
    _description = 'Employee Award'
    _rec_name = 'name'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    award_name = fields.Many2one('award.type', string='Award Type')
    name = fields.Char(string='Name')
    award_date = fields.Date(string='Date')
    award_amount = fields.Float(string='Winning Amount')
    description = fields.Text(string='Description')
    award_given_by = fields.Many2one('hr.employee', string='Award Given By',
                                     domain=[('job_id.name', 'ilike', 'Human Resources Manager')]
                                     , default=lambda self: self.env['hr.employee'].search(
            [('user_id', '=', self.env.uid)], limit=1))

    class HrEmployee(models.Model):
        _inherit = 'hr.employee'

        award_ids = fields.One2many('employee.award', 'employee_id', string="Award Details")
