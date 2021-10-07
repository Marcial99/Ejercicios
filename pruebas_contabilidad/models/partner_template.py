#-*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import UserError
class PartnerTemplate(models.Model):
    _inherit = 'res.partner'


    nuevo = fields.Text(string='Nuevo campo')


   
    @api.model
    def create(self, vals):
        for record in self:
            if not(record.nuevo):
                raise UserError('El campo Nuevo es obligatorio') 
        return super().create(vals)
