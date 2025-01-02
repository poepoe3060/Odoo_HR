from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class KisFerryManagement(models.Model):
    _name = "kis.ferry.management"
    _description = "Kis Ferry Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Ferry Management')
    ferry_id = fields.Many2one('kis.ferry', string="Name", required=True)
    phone = fields.Char(string="Phone")
    car_number = fields.Char(string="Car No")
    ferry_management_line = fields.One2many('kis.ferry.management.line', 'ferry_management_id', string='Ferry Management Lines')
    state = fields.Selection([
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], string='State', store=True)

    def action_confirm(self):
        for ferry in self:
            ferry.state = 'done'
            body = _('Your ferry has been confirmed.')
            ferry.message_post(body=body)
            if not self.ferry_management_line.employee_email:
                raise ValidationError('Employee Mail Required.')
            message = """
                        <div>
                            <p>Dear """ + str(self.ferry_management_line.employee_id.name) + """,</p>
                        </div>
                        <div">
                            <p>Your ferry info has been confirmed by admin team.</p>
                            <p>Thanks.</p>
                        </div>
                        <br>
                        <div">
                            <p>Best regards,</p>
                            <p>Admin Team</p>
                        </div>
                    """
            template_obj = self.env['mail.mail']
            template_data = {
                'subject': 'Ferry Approval Notification',
                'body_html': message,
                'email_from': self.env.user.employee_ids.work_email,
                'email_to': self.ferry_management_line.employee_email,
            }
            template_id = template_obj.create(template_data)
            template_id.send()

    def action_cancel(self):
        self.write({'state': 'cancel'})

    @api.onchange('ferry_id')
    def _onchange_ferry_id(self):
        for ferry in self:
            if ferry.ferry_id:
                self.phone = ferry.ferry_id.phone
                self.car_number = ferry.ferry_id.car_number

class KisFerryManagementLine(models.Model):
    _name = "kis.ferry.management.line"
    _description = "Kis Ferry Management Line"

    ferry_management_id = fields.Many2one('kis.ferry.management', string='Ferry Management', required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee Name", required=True)
    employee_id_code = fields.Char(string='Employee ID')
    employee_email = fields.Char(string='Email', required=True)
    employee_phone = fields.Char(string='Phone')

    @api.model
    def create(self, vals):
        if vals.get('ferry_management_id') and not vals.get('employee_id_code'):
            employee_id_code = self.env['ir.sequence'].next_by_code('employee_id') or _('New')
            vals['employee_id_code'] = employee_id_code
        return super(KisFerryManagementLine, self).create(vals)

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        for management in self:
            if management.employee_id:
                self.employee_email = management.employee_id.work_email
                self.employee_phone = management.employee_id.work_phone
