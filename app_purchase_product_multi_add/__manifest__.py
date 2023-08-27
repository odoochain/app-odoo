# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Multi Add Purchase Product,采购订单批量加产品",
    'version': '14.19.11.19',
    'author': 'odooChain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': """
    App Purchase Order Product Multi Batch Add.
    Odoo App of odooChain.cn
    """,
    'description': """
    App Purchase Order Product Multi Add. 
    1. One Click to add multi product to Purchase Order.
    2. All the product can filter and group.
    采购订单批量增加产品
    1. 可以一键快速将多个产品加到采购订单中
    2. 可对产品进行过滤、分组，然后批量加入
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'purchase',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/purchase_order_views.xml',
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
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
