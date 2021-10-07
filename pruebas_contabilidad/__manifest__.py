#-*- coding:utf-8 -*-
{
    'name':'Prueba contabilidad',
    'summary':'Pruebas de modificaciones al modulo de contabilidad',
    'description':'''
    Se va a modificar el modelo de cliente
    para evitar que se guarde sin telefono
    ''',
    'author':'Juan Pablo Marcial',
    'website':'https://github.com/Marcial99',
    'category':'Training',
    'version':'0.1',
    'depends':[
        'account_accountant',
        'crm'
    ],
    'data':[
        'views/partner_template_views.xml',
        'views/crm_lead_inherit_views.xml'
    ],
    'demo':[]
}