#-*- coding: utf-8 -*-

from odoo import api,fields,models

class PartnerTemplate(models.Model):
    _name = 'res.partner_inherit'
    _inherit = 'res.partner'


    nuevo = fields.Text(string='Nuevo campo')
