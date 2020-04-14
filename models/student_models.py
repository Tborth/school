from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging


class Hospital_Details(models.Model):
    _name = "hospital.details"

    hos_name = fields.Char(string='hos_Name', required=True, copy=False)
    number_bed = fields.Integer(string="number_of_bed")
    email = fields.Char(string="Email")
    


class Corona_Details(models.Model):

    _name ="corona.details"

    country_name =fields.Char(string="Name" )
    
    die_count =fields.Integer(string="die people")



class Patient(models.Model):

    _name ="patient.details"

    name =fields.Char(string="Name")

    age =fields.Integer(string="Age")

    mobile=fields.Char(string="mobile number")

    disease =fields.Selection([('runing noise','runing noise'),('fever','fever'),('corona','corona'),])
    
    email=fields.Char(string='Email')

    fee =fields.Float(compute='check_age')

    @api.depends('age')
    def check_age(self):
        if self.age<18:
            self.fee=500.00
        else:
            self.fee=1000.00
    
    @api.constrains('mobile')
    def check_mobile_number(self):
        if not self.mobile.isdigit():
            raise ValidationError("Please enter valid mobile number")
        if len(self.contact)!=10:
            raise ValidationError("legth of number should be 10")

    