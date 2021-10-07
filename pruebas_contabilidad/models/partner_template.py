#-*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import UserError
class PartnerTemplate(models.Model):
    _inherit = 'res.partner'


    nuevo = fields.Text(string='Nuevo campo')


    @api.constrains('nuevo')
    def _constrains_nuevo(self):
        if len(self.nuevo)<1:
            raise UserError('El campo es obligatorio')