#-*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import UserError
class PartnerTemplate(models.Model):
    _inherit = 'res.partner'


    phone_email = fields.Boolean(compute='_compute_phone_email', string='Verificado')
    
    @api.depends('phone','email')
    def _compute_phone_email(self):
        if (self.phone and self.email):
            self.phone_email=True
        else:
            self.phone_email=False


    @api.constrains('phone')
    def _constrains_phone(self):
        if not(self.phone):
            raise UserError('El telefono es obligatorio') 

    @api.constrains('email')
    def _constrains_email(self):
        if not(self.email):
            raise UserError('El correo electrónico es obligatorio')          