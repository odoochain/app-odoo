# -*- coding: utf-8 -*-

# Created on 2018-11-26
# author: 海南贞人 |  https://www.odoochain.cn
# email: info@odoochain.cn
# resource of odooChain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12在线用户手册（长期更新）
# https://www.odoochain.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odoochain.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odoochain.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odoochain.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odoochain.cn/odoo10_developer_document_offline/
# description:

# Copyright 2017 Simone Orsi
# Copyright 2018 Creu Blanca
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'App Web Fontawesome',
    'version': '14.19.05.30',
    'author': 'odooChain.cn',
    'category': 'Productivity',
    'website': 'https://www.odoochain.cn',
    'license': 'LGPL-3',
    'sequence': 20,
    'images': ['static/description/banner.png'],
    'summary': """Up to date Fontawesome resources. v5.3""",
    'depends': [
        'web',
    ],
    'data': [
        'templates/assets.xml',
    ],
    'installable': True,
    'auto_install': False,
}
