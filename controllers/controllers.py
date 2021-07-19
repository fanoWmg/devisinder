# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
from datetime import datetime


import json


class DevinsiderApi(http.Controller):

    @http.route('/devinsider_api/authenticate', auth='none', type='json')
    def authenticate(self, db, login, password):
        res = request.session.authenticate(db, login, password)
        if res:
            message = "connection reussi"
        else:
            message = "connection non reussi"
        headers = {'Content-Type': 'application/json'}
        result = {
            'data': message,
            'error': {},
            'meta': {},
        }
        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/create_compte', auth="user", type='http')
    def create_compte(self, user_name, **k):
        headers = {'Content-Type': 'application/json'}
        devinsider_obj = request.env['devinsider_api.compte']
        mail_template_obj = request.env.ref('devinsider_api.mail_template_user_signup_account_created_devinsider')
        type_mail = request.env.ref('devinsider_api.data_send_mail_for_create_compte')
        login_exist = devinsider_obj.search([('user_name', '=', user_name)])

        if not login_exist:
            devinsider_obj.sudo().create({
                'user_name': user_name,
                'mail_template_id': mail_template_obj.id,
                #''
            })
        compte = devinsider_obj.search([('user_name', '=', user_name)], limit=1)

        request.env['devinsider_api.mail_backup'].sudo().create({
            'name': datetime.now(),
            'user_mail_id': compte.id,
            'type_mail_id': type_mail.id,
        })
        email_values = {
            'email_to': user_name,
            'user_mail_id': compte.id,
            'type_mail_id': type_mail.id,
        }
        try:
            mail_template_obj.write({'auto_delete': False})
            mail_template_obj.with_context(lang=http.request.env.user.lang).send_mail(compte.id,
                                                                                  force_send=True,
                                                                                  raise_exception=True,
                                                                                  email_values=email_values)
            message = "email is send"
        except:
            message = "email not send"



        result = {
            'message': message,
            'data': {},
            'error': {},
            'meta': {},
        }
        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/reset_password', auth="user", type='http')
    def reset_password(self, id_mail, user_name, **k):
        message = ""
        compte = http.request.env['devinsider_api.compte'].search([('id_mail', '=', id_mail)])
        if not compte:
            create_new_compte = compte.sudo().create({
                'user_name': user_name,
                'id_mail': id_mail,
            })
            if create_new_compte:
                compte = http.request.env['devinsider_api.compte'].search([('id_mail', '=', id_mail)])
        email_values = {
            'email_to': user_name
        }
        mail_template_obj = http.request.env.ref('devinsider_api.template_mail_reset_password_email_devinsider')
        mail_template_obj.write({'auto_delete': False})
        mail_sent = mail_template_obj.with_context(lang=http.request.env.user.lang).send_mail(compte.id,
                                                                                              force_send=True,
                                                                                              raise_exception=True,
                                                                                              email_values=email_values)
        if mail_sent:

            mail_obj.browse(max(list_mail_id)).write({
                # 'subject': mail_template_obj.subject,
                'body_html': mail_template_obj.body_html,

            })
            message = "mail has sent"
        else:
            message = "mail not sent"

        headers = {'Content-Type': 'application/json'}
        result = {
            'message': message,
            'error': {},
            'meta': {},
        }

        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/update_mail', type='http', auth="user")
    def update_mail(self, compte_id, new_email, **k):
        headers = {'Content-Type': 'application/json'}
        compte_obj = http.request.env['devinsider_api.compte'].search([('id', '=', int(compte_id))])
        if compte_obj:
            if compte_obj.email != new_email:
                compte_obj.sudo().write({
                    'email': new_email
                })
                message = "successful mail update!!"
            else:
                message = "mail already exist"
        else:
            message = "you have not account"
        result = {
            'message': message,
            'data': {},
            'error': {},
            'meta': {},
        }
        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/become_pro_with_mail_pro', type='http', auth="user")
    def become_pro_with_mail_pro(self, email_pro, compte_id, **k):
        compte_obj = http.request.env['devinsider_api.compte'].search([('id', '=', int(compte_id))])
        if compte_obj and email_pro:
            compte_obj.write({
                'email_pro': email_pro
            })
            message = "successful save mail pro"
        else:
            message = "No account"
        headers = {'Content-Type': 'application/json'}
        result = {
            'message': message,
            'data': {},
            'error': {},
            'meta': {},
        }
        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/become_pro_with_mail_normal', type='http', auth="user")
    def become_pro_with_mail_normal(self, compte_id, phone_number, email_pro, message_text, verified_professional):
        compte_obj = http.request.env['devinsider_api.compte'].search([('id', '=', int(compte_id))])
        if compte_obj:
            compte_obj.write({
                'email_pro': email_pro,
                'phone_number': phone_number,
                'message_text': message_text,
                'verified_professional': verified_professional
            })
            pass
