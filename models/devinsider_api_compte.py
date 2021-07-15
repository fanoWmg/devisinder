# -*- coding: utf-8 -*-


from odoo import models, fields, api


class devinsider_api(models.Model):
    _name = 'devinsider_api.compte'

    name = fields.Char(string="Name")
    user_name = fields.Char(string="Email")
    email_pro = fields.Char(string="Email pro")
    company_id = fields.Many2one(string="Company")
    mail_template_id = fields.Many2one('mail.template', string="Mail template")

    # become pro
    phone_number = fields.Char(string="Phone number")
    message_text = fields.Text(string="Text message")
    verified_professional = fields.Boolean(string="verified profesional")
    number_mail = fields.Integer(string="Number mail", compute="_compute_number_mail")

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
        mail_list = []
        res = ""
        mail_obj = self.env['mail.mail']
        mail = mail_obj.search([('user_mail_id', '=', user_name_id)])
        for m in mail:
            mail_list.append(m.id)
        max_id_mail_user = max(mail_list)
        type_mail = mail_obj.browse(max_id_mail_user).mapped('type_mail_id')
        for t in type_mail:
           if detail == 'title':
                res = t.title
           if detail == 'description':
               res = t.mail_desciption
        return res
