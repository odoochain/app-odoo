# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "App HR department ztree, parent children tree",
    'version': '14.19.09.27',
    'author': 'odooChain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Use for parent children tree list select navigator. hr department employee tree.
    ztree widget.
    """,
    'description': """
    zTree widget.
    Advance search with real parent children tree, ListView or KanbanView ,
    eg: Product category tree ,Department tree, stock location tree.
    超级方便的查询，树状视图。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'hr',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/hr_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
