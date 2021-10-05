#-*- coding: utf-8 -*-

from odoo import api,fields,models

class PartnerTemplate(models.Model):
    _inherit = 'res.partner'


    nuevo = fields.Text(string='Nuevo campo')
