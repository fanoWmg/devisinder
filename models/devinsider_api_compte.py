# -*- coding: utf-8 -*-


from odoo import models, fields, api
from datetime import datetime


class devinsider_api(models.Model):
    _name = 'devinsider_api.compte'

    name = fields.Char(string="Name", readonly=True)
    user_name = fields.Char(string="Email",  readonly=True)
    email_pro = fields.Char(string="Email pro",  readonly=True)
    company_id = fields.Many2one(string="Company")
    mail_template_id = fields.Many2one('mail.template', string="Mail template")

    # become pro
    phone_number = fields.Char(string="Phone number", readonly=True)
    message_text = fields.Text(string="Text message", readonly=True)
    verified_professional = fields.Boolean(string="verified profesional",  readonly=True)
    number_mail = fields.Integer(string="Number mail", compute="_compute_number_mail",  readonly=True)

    def send_mail_data(self, mail_template_obj, user_name, type_mail):
        devinsider_obj = self.env['devinsider_api.compte']
        compte = devinsider_obj.search([('user_name', '=', user_name)], limit=1)
        self.env['devinsider_api.mail_backup'].sudo().create({
            'name': datetime.now(),
            'user_mail_id': compte.id,
            'type_mail_id': type_mail.id,
        })
        print(user_name)
        email_values = {
            'email_to': user_name,
            'user_mail_id': compte.id,
            'type_mail_id': type_mail.id,
        }
        mail_server = self.env['ir.mail_server'].search([('is_devinsider_out_going', '=', True)])
        mail_template_obj.write({'auto_delete': False, 'mail_server_id': mail_server.id})
        mail_template_obj.with_context(lang=self.env.user.lang).send_mail(compte.id,
                                                                                  force_send=True,
                                                                                  raise_exception=True,
                                                                                  email_values=email_values)

    @api.depends('user_name')
    def _compute_number_mail(self):
        for rec in self:
            mail = rec.env['mail.mail'].search([('email_to', '=', rec.user_name)])
            rec.number_mail = len(mail)

    def list_user_mail(self):
        domain = [('email_to', '=', self.user_name)]
        mail_list_res_id = self.env.ref('mail.view_mail_tree').id
        return {
            'name': 'Mail liste send to %s' % (self.user_name),
            'type': 'ir.actions.act_window',
            'view_mode': 'list',  # tsy mety ref miclick mail ray ao am list
            'res_model': 'mail.mail',
            'res_id': mail_list_res_id,
            'domain': domain
        }

    def get_mail_info(self, user_name_id, detail):
        res = "tsisy"
        type_mail_obj = self.env['devinsider_api.type_mail']
        last_mail = self.env['devinsider_api.mail_backup'].search([('user_mail_id', '=', user_name_id)],
                                                                  order="id desc", limit=1)
        if detail == 'title':
            res = type_mail_obj.browse(last_mail.type_mail_id).title
        if detail == 'description':
            res = type_mail_obj.browse(last_mail.type_mail_id).mail_desciption
        return res
