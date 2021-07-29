# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(string="First name")
    last_name = fields.Char(string="Last name")


    contact_category = fields.Selection([
        ('software_vendor', 'Software Vendor'),
        ('reseller', 'Reseller'),
        ('gest', 'Gest'),
        ('expert_contributor', 'Expert Contributor'),
        ('institutional_investor', 'Institutional Investor'),
        ('individual_investor', 'Individual Investor'),
        ('partner_program', 'Partner Program'),
    ],
        string='Contact Category')

    contact_status = fields.Selection([
        ('not_registered_in_di', 'Not Registered On Devinsider'),
        ('registered_in_di', 'Registered On Devinsider')],
        string='Contact Status')

    job_position = fields.Char(string='Job Position')

    job_category = fields.Selection([
        ('executive_management', 'Executive Management'),
        ('finance_and_accounting', 'Finance and Accounting'),
        ('general_administration', 'General Administration'),
        ('human_resources', 'Human Resources'),
        ('it', 'IT'),
        ('legal', 'Legal'),
        ('logistics_and_supply_chain', 'Logistics and Supply Chain'),
        ('marketing', 'Marketing'),
        ('operations_production', 'Operations / Production'),
        ('partner_alliances', 'Partner / Alliances'),
        ('purchasing_and_procurement', 'Purchasing and Procurement'),
        ('quality_and_change_management', 'Quality and Change Management'),
        ('research_and_development', 'Research and Development'),
        ('sales', 'Sales'),
        ('service_and_support', 'Service and Support'),
        ('web', 'Web')],
        string='Job catergory')

    job_level = fields.Selection([
        ('c_level', 'C - Level'),
        ('vp', 'VP'),
        ('director', 'Director'),
        ('manager', 'Manager'),
        ('assistant', 'Assistant'),
        ('non_dm', 'Non - DM'),
        ('other_dm', 'Other DM')],
        string='Job level')

    linkedin = fields.Char(string='Linkedin')

    notes = fields.Text(string='Notes')

    ###### DI Mirror ######

    di_name = fields.Char(string='Name')

    di_fistname = fields.Char(string='Firstname')

    di_lastname = fields.Char(string='Larstname')

    di_image_profil = fields.Binary(string='.')

    di_job_position = fields.Char(string='Job position')

    di_city = fields.Char(string='City')

    di_country_id = fields.Many2one('res.country', 'Country')

    di_primary_email = fields.Char(string='Primary Email')

    di_work_email = fields.Char(string='Work Email')

    di_phone = fields.Char(string='Phone')

    di_linkedin = fields.Char(string='Linkedin')

    di_about = fields.Text(string='About')

    @api.onchange('first_name', 'last_name')
    def onchange_first_last_name(self):
        name = self.name
        if self.company_type == 'person':
            if self.first_name or self.last_name:
                name_tab = [self.first_name or '', self.last_name or '']
                name = ' '.join(name_tab)
            else:
                name = False
        self.name = name

    def create_partner_type_person(self, first_name, last_name, parent):
        partner = self.search([('last_name', '=', last_name), ('first_name', '=', first_name)])
        last_name = False if last_name == "" else last_name
        first_name = False if first_name == "" else first_name
        if not partner and (last_name or first_name):
            name_tab = [first_name or '', last_name or '']
            name = ' '.join(name_tab)
            partner = self.create({
                'first_name': first_name,
                'last_name': last_name,
                'parent_id': parent.id,
                'name': name,
                'company_type': 'person'
            })
        return partner
