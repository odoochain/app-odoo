# -*- coding: utf-8 -*-

{
    'name': "App product browse by category navigator",
    'version': '16.23.09.01',
    'author': 'odooai.cn, odoochain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'live_test_url': 'https://demo.odoochain.cn',
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
    'images': ['static/description/banner.png'],
    'data': [
        'views/product_template_views.xml',
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
