# -*- coding: utf-8 -*-

# Created on 20120-01-05
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

##############################################################################
#    Copyright (C) 2009-TODAY odooChain.cn Ltd. https://www.odoochain.cn
#    Author: info@odoochain.cn
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "odooChain Odooapp Common Func",
    'version': '14.21.10.18',
    'author': 'odooChain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Core for common use sunpop apps.
    基础核心，必须没有要被依赖字段及视图等，实现auto_install
    ''',
    'description': '''    
    Support Odoo 14,13,12, Enterprise and Community Edition
    1. 
    2. 
    3. Multi-language Support.
    4. Multi-Company Support.
    5. Support Odoo 14,13,12, Enterprise and Community Edition
    ''',
    'depends': [
        'base',
        'web',
        'product',
    ],
    'data': [
        # 'security/*.xml',
        # 'security/ir.model.access.csv',
        # 'data/.xml',
        'views/ir_cron_views.xml',
        'views/webclient_templates.xml',
        # 'report/.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
