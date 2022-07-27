# -*- coding: utf-8 -*-

# Created on 2018-11-05
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "mixin english name，增加英文名字段",
    'version': '14.20.05.11',
    'author': 'odooChain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0,
    'currency': 'EUR',
    'summary': """
    Chinese enhance. Out of the box use in china.
    Set all chinese default value.
    Add quick set of english name.
    Default country, timezone, currency, partner... 
    """,
    'description': """
    
    odoo Chinese Enhance. 中国化增强-基础
    1. mixin, 增加英文名字段, 自动设定lang=en_US的名称为英文名  
    2
    """,
    'depends': [
        'base',
    ],
    'images': ['static/description/banner.jpg'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
