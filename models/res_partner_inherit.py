# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(string="First name")
    last_name = fields.Char(string="Last name")
    email_score = fields.Boolean(string="Email Score")
    email_hard_bounced = fields.Char(string="Email Hard Bounced")
    email_soft_bounced = fields.Char(string="Email Soft Bounced")
    email_pro = fields.Char(string="Email")
    company_type = fields.Selection(string='Company Type',
                                    selection=[('person', 'Individual'), ('company', 'Company')],
                                    compute='_compute_company_type', inverse='_write_company_type', default='person')




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


    notes = fields.Text(string='Notes')

    ###### DI Mirror ######

    di_name = fields.Char(string='Name', readonly=True)
    di_fistname = fields.Char(string='First Name', readonly=True)
    di_lastname = fields.Char(string='Last Name', readonly=True)
    #di_image_profil = fields.Binary(string='.', readonly=True)
    di_job_position = fields.Char(string='Job position', readonly=True)
    di_city = fields.Char(string='City', readonly=True)
    di_country_id = fields.Many2one('res.country', 'Country', readonly=True)
    di_primary_email = fields.Char(string='Primary Email', readonly=True)
    di_work_email = fields.Char(string='Work Email', readonly=True)
    di_phone = fields.Char(string='Phone', readonly=True)
    di_linkedin = fields.Char(string='Linkedin', readonly=True)
    di_about = fields.Text(string='About', readonly=True)
    di_email_email_score = fields.Char(string="Email score")
    di_email_hard_bounced = fields.Char(string="Email Hard Bounced")
    di_email_soft_bounced = fields.Char(string="Email Soft Bounced")
    di_first_name_po = fields.Char(string="First Name")
    di_last_name_po = fields.Char(string="Last Name")
    di_job_location = fields.Char(string="Location")

    @api.onchange('first_name', 'last_name')
    def onchange_first_last_name(self):
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
