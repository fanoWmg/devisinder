# -*- coding: utf-8 -*-


from odoo import models, fields, api


class MailMailInherit(models.Model):
     _inherit = 'mail.mail'

     type_mail_id = fields.Many2one('devinsider_api.type_mail', string="Mail type")
     user_mail_id = fields.Many2one('devinsider_api.compte', string="User mail")

     def write(self, vals):
        if vals.get('type_mail_id') == self.env.ref('devinsider_api.data_send_mail_for_create_compte').id:
            vals['type_mail_id'] = self.env.ref('devinsider_api.data_send_mail_for_create_compte').id
        return super(MailMailInherit, self).write(vals)

class Mailbackup(models.Model):
    _name = 'devinsider_api.mail_backup'

    name = fields.Datetime('Name')
    user_mail_id = fields.Integer('user_mail_id')
    type_mail_id = fields.Integer('type_mail_id')


class devinsider_type_mail(models.Model):
    _name = 'devinsider_api.type_mail'

    name = fields.Char(string="Mail type")
    title = fields.Char(string="Title")
    mail_desciption = fields.Char(string="description")
