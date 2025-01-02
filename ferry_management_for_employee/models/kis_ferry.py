from odoo import fields, models, _


class KisFerry(models.Model):
    _name = "kis.ferry"
    _description = "Kis Ferry"

    name = fields.Char(string="Ferry Name", required=True)
    phone = fields.Char(string="Phone", required=True)
    car_number = fields.Char(string="Car No", required=True)
    address = fields.Char(string="Address")