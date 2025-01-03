from odoo import models, fields, api, _


class EmployeePaySlip(models.Model):
    _name = "employee.payslip"
    _description = 'Kings Employee Pay Slip'

    name = fields.Many2one('hr.employee',string="Employee Name")
    staff_id = fields.Char(string="Staff ID")
    department_id = fields.Many2one('hr.department',string="Department")
    job_id = fields.Many2one('hr.job',string="Designation")
    start_date = fields.Date(string="Join Date")
    service_year = fields.Char(string="Month/Year")


