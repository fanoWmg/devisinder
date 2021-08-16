# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
from . import main


class CrmController(http.Controller):

    @http.route('/devinsider_api/create_crm_lead', auth='public', type='json')
    def create_crm_lead(self, name_lead, first_name, last_name, company_name, company_type):
        status = 200
        all_message = []
        company = ['person', 'company']
        main.DevinsiderConnection.__init__(main)
        res_partner = request.env['res.partner']
        crm_lead = request.env['crm.lead']
        crm_company = res_partner.search([('name', '=', company_name)], limit=1)
        if not crm_company:
            crm_company = res_partner.sudo().create({
                'name': company_name,
            })
        parent = crm_company
        partner_type_person_have_created = res_partner.create_partner_type_person(first_name, last_name, parent)
        if partner_type_person_have_created and company_type == 'person':
            request.env['crm.lead'].create({
                'is_devinsider_lead': True,
                'name': name_lead,
                'partner_id': partner_type_person_have_created.id,
                'type': 'opportunity',
            })
            crm = request.env['crm.lead'].search([('name', "=", name_lead)], limit=1)
            message = "crm person created => crm_id = %s" % (crm.id)
            all_message.append(message)
        if not partner_type_person_have_created and company_type == 'company':
            crm_lead.sudo().create({
                'is_devinsider_lead': True,
                'name': name_lead,
                'partner_id': crm_company.id,
                'type': 'opportunity',
            })
            crm = request.env['crm.lead'].search([('name', "=", name_lead)], limit=1)
            message = "crm company created => crm_id = %s" % (crm.id)
            all_message.append(message)
        if not partner_type_person_have_created and company_type == 'person':
            message = "first name or last name invalid"
            all_message.append(message)

        if company_type not in company:
            message = "company_type must be company or person"
            all_message.append(message)

        if partner_type_person_have_created and company_type == 'company':
            message = "company have not first name or last name"
            all_message.append(message)
        return {
            'status': status,
            'message': all_message
        }
