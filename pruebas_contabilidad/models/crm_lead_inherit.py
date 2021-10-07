#-*- coding:utf-8 -*-
from odoo import  api, fields, models

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    birthday = fields.Date(string='Birthday')
    