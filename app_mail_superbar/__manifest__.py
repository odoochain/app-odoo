# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Mail quick navigator,mail filter",
    'version': '14.19.10.16',
    'author': 'odooChain.cn',
    'category': 'Base',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': """
    mail search, browse all mail by all kind of category. Use for parent children tree list kanban navigator. 
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
        'mail',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/mail_channel_partner_views.xml',
        'views/mail_followers_views.xml',
        'views/mail_mail_views.xml',
        'views/mail_message_views.xml',
        'views/mail_tracking_value_views.xml',
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
