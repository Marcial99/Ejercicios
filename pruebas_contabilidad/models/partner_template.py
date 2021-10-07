#-*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import UserError
class PartnerTemplate(models.Model):
    _inherit = 'res.partner'


    nuevo = fields.Text(string='Nuevo campo')


    @api.constrains('phone')
    def _constrains_phone(self):
        if not(self.phone):
            raise UserError('El telefono es obligatorio') 

    @api.constrains('email')
    def _constrains_email(self):
        if not(self.email):
            raise UserError('El correo electrónico es obligatorio')          