# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/

{
    'name': 'App Web Responsive Fullwidth (form view full width)',
    'version': '16.23.02.19',
    'category': 'web',
    'author': 'odooai.cn',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    "price": 18.00,
    "currency": "EUR",
    'images': ['static/description/banner.png'],
    'summary': """
    Form view Responsive full width (fullwidth). Ready for small, medium, large, extra large screen.Ready for enterprise and communicate version.
    """,
    'description': """
    UI Enhance for Odoo. Form view fullwidth, full screen.
    ready
    """,
    'depends': [
        'web'
    ],
    'data': [],
    'assets': {
        'web.assets_backend': [
            ('after', 'web/static/src/views/**/*', 'app_web_fullwidth/static/src/scss/app_style_after.scss'),
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': True,
}
