# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
from datetime import datetime


import json

#test en dev
DB = "crm"
LOGIN = "arthur@mediadev.com"
PSWD = "Qwerty789"

 #test local
#DB = "devisinder"
#LOGIN = "admin"
#PSWD = "admin1234"


class DevinsiderApi(http.Controller):

    @http.route('/devinsider_api/authenticate', auth='none', type='json')
    def authenticate(self, db, login, password):
        try:
            request.session.authenticate(db, login, password)
            status = 200
        except:
            status = 400
        return {
            'status': status
        }

    @http.route('/devinsider_api/create_compte', auth="public", type='http')
    def create_compte(self, user_name, **k):
        request.session.authenticate(DB, LOGIN, PSWD)
        headers = {'Content-Type': 'application/json'}
        mail_template_obj = request.env.ref('devinsider_api.mail_template_user_signup_account_created_devinsider')
        type_mail = request.env.ref('devinsider_api.data_send_mail_for_create_compte')
        devinsider_obj = request.env['devinsider_api.compte']
        login_exist = devinsider_obj.search([('user_name', '=', user_name)])
        if not login_exist:
            devinsider_obj.sudo().create({
                'user_name': user_name,
                'mail_template_id': mail_template_obj.id,
            })
        try:
            devinsider_obj.send_mail_data(mail_template_obj, user_name, type_mail)
            message = "email is send"
            status = 200
        except:
            message = "email not send"
            status = 400

        result = {
            'message': message,
            'status': status,
        }
        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/reset_password', auth="public", type='http')
    def reset_password(self, user_name, **k):
        request.session.authenticate(DB, LOGIN, PSWD)
        headers = {'Content-Type': 'application/json'}
        devinsider_obj = request.env['devinsider_api.compte']
        mail_template_obj = request.env.ref('devinsider_api.mail_template_for_reset_password')
        type_mail = request.env.ref('devinsider_api.data_send_mail_for_password_reset')
        login_exist = devinsider_obj.search([('user_name', '=', user_name)])
        if not login_exist:
            devinsider_obj.sudo().create({
                'user_name': user_name,
            })
        try:
            devinsider_obj.send_mail_data(mail_template_obj, user_name, type_mail)
            message = "email is send for reset password"
            status = 200
        except:
            message = "email not send"
            status = 400

        result = {
            'message': message,
            'status': status,
        }
        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/update_mail', type='http', auth="public")
    def update_mail(self, user_name, new_email, **k):
        request.session.authenticate(DB, LOGIN, PSWD)
        headers = {'Content-Type': 'application/json'}
        devinsider_obj = request.env['devinsider_api.compte']
        mail_template_obj = request.env.ref('devinsider_api.update_mail_devinsider')
        type_mail = request.env.ref('devinsider_api.data_send_mail_for_update_mail')
        login_exist = devinsider_obj.search([('user_name', '=', user_name)])
        if not login_exist:
            devinsider_obj.sudo().create({
                'user_name': user_name,
            })
        compte = devinsider_obj.search([('user_name', '=', user_name)])
        compte.write({
           'user_name': new_email,
       })
        try:
            devinsider_obj.send_mail_data(mail_template_obj, new_email, type_mail)
            message = "email is send for update_mail"
            status = 200
        except:
            message = "email not send"
            status = 400

        result = {
            'message': message,
            'status': status,
        }
        return Response(json.dumps(result), headers=headers)

    @http.route('/devinsider_api/become_pro', type='json', auth="public")
    def become_pro(self, user_name, name, phone_number, message_text, **k):
        request.session.authenticate(DB, LOGIN, PSWD)
        mail_template_obj = request.env.ref('devinsider_api.mail_template_user_verified_pro')
        type_mail = request.env.ref('devinsider_api.data_send_mail_for_verified_pro')
        compte_obj = http.request.env['devinsider_api.compte'].search([('user_name', '=', user_name)])
        devinsider_obj = request.env['devinsider_api.compte']
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
            devinsider_obj.send_mail_data(mail_template_obj, user_name, type_mail)
            message = "successful save mail pro"
            status = 200
        except:
            message = "mail for mail pro not send"
            status = 400
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

