# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': "App product browse by category navigator",
    'version': '14.21.08.29',
    'author': 'odooChain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Browse Product by category tree. Use for parent children tree list kanban navigator. 
    Easy to navigator and browse any data. Support list, kanban, pivot, graph view. 
    ztree widget.Hierarchy Tree.Parent Children relation tree..
    """,
    'description': """
    Superbar, zTree widget. 
    Advance search with real parent children tree, ListView or KanbanView. parent tree, children tree,
    Product category tree ,Department tree, stock location tree.
    超级方便的查询，树状视图
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'stock',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/product_views.xml',
        'views/product_category_views.xml',
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
