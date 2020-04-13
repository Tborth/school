from odoo import models, fields, api
import logging


class Hospital_Details(models.Model):
    _name = "hospital.details"

    hos_name = fields.Char(string='Name', required=True, copy=False)
    number_bed = fields.Integer(string="number of bed")
    email = fields.Char(string="Email")

class Corona_Details(models.Model):

    _name ="corona.details"

    country_name =fields.Char(string="Name" )
    
    die_count =fields.Integer(string="die people")

class Patient(models.Model):

    _name ="patient.details"

    name =fields.Char(string="Name")

    age =fields.Integer(string="Age")

    mobile=fields.Integer(string="mobile number")

    disease =fields.Selection([('runing noise','runing noise'),('fever','fever'),('corona','corona'),])
    
    email=fields.Char(string='Email')