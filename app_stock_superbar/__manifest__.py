# -*- coding: utf-8 -*-


{
    'name': "Stock Superbar ztree, parent children tree",
    'version': '16.23.08.31',
    'author': 'odooai.cn,odoochain',
    'category': 'Warehouse',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Use for parent children tree list select navigator. stock location tree, filter by parent location.
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
        'stock',
        'stock_picking_batch',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/stock_location_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_type_views.xml',
        'views/stock_warehouse_orderpoint_views.xml',
        'views/stock_rule_views.xml',
        'views/stock_lot_views.xml',
        # todo: 以下两个模型调整了
        # 'views/stock_location_route_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    # 'qweb': [
    #     'static/src/xml/*.xml',
    # ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
