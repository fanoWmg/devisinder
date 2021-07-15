# -*- coding: utf-8 -*-


from odoo import models, fields, api


class MailMailInherit(models.Model):
     _inherit = 'mail.mail'

     type_mail_id = fields.Many2one('devinsider_api.type_mail', string="Mail type")
     user_mail_id = fields.Many2one('devinsider_api.compte', string="User mail")


class devinsider_type_mail(models.Model):
    _name = 'devinsider_api.type_mail'

    name = fields.Char(string="Mail type")
    title = fields.Char(string="Title")
    mail_desciption = fields.Char(string="description")
