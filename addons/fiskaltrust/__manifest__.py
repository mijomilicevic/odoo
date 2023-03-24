# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'fiskaltrust',
    'version': '1.0',
    'category': 'POS',
    'sequence': 15,
    'summary': 'Fiskalization',
    'description': "",
   # 'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'base',
        'pos_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_config.xml',
    ],
    'demo': [
    ],
    'css': []
}

