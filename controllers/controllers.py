# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
from datetime import datetime


import json


class DevinsiderApi(http.Controller):

    @http.route('/devinsider_api/authenticate', auth='none', type='json')
    def authenticate(self, db, login, password):
        try:
            request.session.authenticate(db, login, password)
            status = 200
        except:
            status = 400
        return {
            'status':status
        }

    @http.route('/devinsider_api/get_session_info', type='json', auth="none")
    def get_session_info(self):

        a = request.session.check_security()
        a
        print(a)

        request.uid = request.session.uid
        request.disable_db = False
        return request.env['ir.http'].session_info()


    @http.route('/devinsider_api/create_compte', auth="public", type='http')
    def create_compte(self, user_name, **k):
        request.session.authenticate("base64", "admin", "admin")
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
            mail_server = request.env['ir.mail_server'].search([('is_devinsider_out_going', '=', True)])
            mail_template_obj.write({'auto_delete': False, 'mail_server_id': mail_server.id})
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
    def reset_password(self, user_name, **k):
        headers = {'Content-Type': 'application/json'}
        devinsider_obj = request.env['devinsider_api.compte']
        mail_template_obj = request.env.ref('devinsider_api.mail_template_for_reset_password')
        type_mail = request.env.ref('devinsider_api.data_send_mail_for_password_reset')
        login_exist = devinsider_obj.search([('user_name', '=', user_name)])
        if not login_exist:
            devinsider_obj.sudo().create({
                'user_name': user_name,
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
            mail_server = request.env['ir.mail_server'].search([('is_devinsider_out_going', '=', True)])
            mail_template_obj.write({'auto_delete': False, 'mail_server_id': mail_server.id})
            mail_template_obj.with_context(lang=http.request.env.user.lang).send_mail(compte.id,
                                                                                      force_send=True,
                                                                                      raise_exception=True,
                                                                                      email_values=email_values)
            message = "email is send for reset password"
        except:
            message = "email not send"

        return {
            'message': message
        }

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

    @http.route('/devinsider_api/become_pro', type='json', auth="public")
    def become_pro(self, user_name, name, phone_number, message_text, **k):
        request.session.authenticate("devisinder", "admin", "admin1234")
        mail_template_obj = request.env.ref('devinsider_api.mail_template_user_verified_pro')
        type_mail = request.env.ref('devinsider_api.data_send_mail_for_verified_pro')
        compte_obj = http.request.env['devinsider_api.compte'].search([('user_name', '=', user_name)])
        if compte_obj:
            compte_obj.write({
                'email_pro': user_name,
                'name': name,
                'phone_number': phone_number,
                'message_text': message_text,
            })
        else:
            request.env['devinsider_api.compte'].sudo().create({
                'user_name': user_name,
                'email_pro': user_name,
                'name': name,
                'phone_number': phone_number,
                'message_text': message_text,
            })

        try:
            request.env['devinsider_api.mail_backup'].sudo().create({
                'name': datetime.now(),
                'user_mail_id': compte_obj.id,
                'type_mail_id': type_mail.id,
            })
            email_values = {
                'email_to': user_name,
                'user_mail_id': compte_obj.id,
                'type_mail_id': type_mail.id,
            }
            mail_server = request.env['ir.mail_server'].search([('is_devinsider_out_going', '=', True)])
            mail_template_obj.write({'auto_delete': False, 'mail_server_id': mail_server.id})
            mail_template_obj.with_context(lang=http.request.env.user.lang).send_mail(compte_obj.id,
                                                                                              force_send=True,
                                                                                              raise_exception=True,
                                                                                              email_values=email_values)

            message = "successful save mail pro"
            status = 200
        except:
            message = "mail for mail pro not send"
            status = 400

        #headers = {'Content-Type': 'application/json'}
        # result = {
        #     'message': message,
        #     'data': {},
        #     'error': {},
        #     'meta': {},
        # }
        return {
            'message': message,
            'status': status
        }

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

