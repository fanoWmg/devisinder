# -*- coding: utf-8 -*-


from odoo import models, fields, api


class MailTemplateInherit(models.Model):
     _inherit = 'mail.template'

     title = fields.Char(string="Title")
     mail_desciption = fields.Char(string="description")