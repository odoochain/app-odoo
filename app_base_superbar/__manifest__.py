# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Easy Admin navigator, quick search filter",
    'version': '14.20.04.06',
    'author': 'odooChain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': """
    menu admin, fields admin, action admin, views easy admin and search, quick admin navigator by all kind of category. Use for parent children tree list kanban navigator. 
    ztree widget.Hierarchy Tree.Parent Children relation tree..
    """,
    'description': """
    Superbar, zTree widget. 
    Advance search with real parent children tree, ListView or KanbanView. parent tree, children tree,
    eg: Product category tree ,Department tree, stock location tree.
    超级方便的查询，树状视图。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'web',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        # 'views/res_groups_views.xml',
        'views/ir_actions_act_window_views.xml',
        'views/ir_actions_actions_views.xml',
        'views/ir_actions_report_views.xml',
        'views/ir_actions_server_views.xml',
        'views/ir_attachment_views.xml',
        'views/ir_default_views.xml',
        'views/ir_model_access_views.xml',
        'views/ir_model_constraint_views.xml',
        'views/ir_model_fields_views.xml',
        'views/ir_ui_menu_views.xml',
        'views/ir_ui_view_views.xml',
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
