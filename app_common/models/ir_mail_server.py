# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging

_logger = logging.getLogger(__name__)


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"
    _order = "sequence"

    # 改默认发邮件逻辑
    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None,  *args, **kwargs):

        email_to = message['To']

        # 忽略掉无效email，避免被ban
        if email_to.find('no-reply@lawia.org.cn') != -1 or email_to.find('postmaster-odoo@lawia.org.cn') != -1:
            pass
        elif email_to.find('@example.com') != -1:
            _logger.error(_("=================Email to ignore: %s") % email_to)
            raise AssertionError(_("Email to ignore: %s") % email_to)

        return super(IrMailServer, self).send_email(message, mail_server_id, smtp_server, *args, **kwargs)
