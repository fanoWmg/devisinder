# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(string="First name")
    last_name = fields.Char(string="Last name")
    email_score = fields.Boolean(string="Email Score")
    email_hard_bounced = fields.Boolean(string="Email Hard Bounced")
    email_soft_bounced = fields.Boolean(string="Email Soft Bounced")
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
    di_contact_status = fields.Char(string='Contact Status')

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
    di_email_pro = fields.Char(string='Email', readonly=True)
    di_fistname = fields.Char(string='First Name', readonly=True)
    di_lastname = fields.Char(string='Last Name', readonly=True)
    # di_image_profil = fields.Binary(string='.', readonly=True)
    di_job_position = fields.Char(string='Job position')
    di_city = fields.Char(string='City', readonly=True)
    di_country_id = fields.Many2one('res.country', 'Country', readonly=True)
    di_primary_email = fields.Char(string='Primary Email', readonly=True)
    di_work_email = fields.Char(string='Work Email', readonly=True)
    di_phone = fields.Char(string='Phone', readonly=True)
    di_linkedin = fields.Char(string='Linkedin', readonly=True)
    di_about = fields.Text(string='About', readonly=True)
    di_email_email_score = fields.Char(string="Email score")
    di_email_hard_bounced = fields.Boolean(string="Email Hard Bounced")
    di_email_soft_bounced = fields.Boolean(string="Email Soft Bounced")
    di_first_name_po = fields.Char(string="First Name")
    di_last_name_po = fields.Char(string="Last Name")
    di_job_location = fields.Char(string="Location")

    di_contact_category = fields.Char(string="Contact Category")
    di_contact_status = fields.Char(string="Contact Status")
    di_date_signup = fields.Date(string="Date of Sign-Up")
    di_date_last_login = fields.Date(string="Date of the last Log-In")
    di_active_company_page = fields.Boolean(string="Active Company Page (Created, affiliated or Claimed Ownership)")
    di_date_creation_claimed_own = fields.Date(string="Date of Creation/Claimed Ownership")
    # Mirror Comminity
    di_discussion_categ_followed = fields.Char(string="Discussion Categorie Followed")
    di_label_followed = fields.Char(string="Label Followed")
    di_date_last_forum_contrib = fields.Char(string="Date of the last Forum Contribution")
    di_amount_forum_created = fields.Char(string="Amount of Forum Created")
    di_amount_forum_replie = fields.Char(string="Amount of Forum replies")
    di_amount_replie_qualified_best_answer = fields.Char(string='Amount of replies qualified as "Best Answer"')
    di_date_last_article_contrib = fields.Char(string="Date of the last Article Contributions")
    di_amount_article_created = fields.Char(string="Amount of article Created")
    di_date_last_pres_realese_contrib = fields.Char(string="Date of the Last Press Release Contribution")
    di_amount_press_release_created = fields.Char(string="Amount of Press Releases Created")
    di_date_last_programme_reviews_contrib = fields.Char(string="Date of the last Program Reviews Contributions")
    di_amount_programme_reviews = fields.Char(string="Amount of Program Review Created")
    di_community_profil_description = fields.Char(string="Community Profil Description")
    # Classified Ads
    di_date_last_ads_contrib = fields.Date(string="Date of Last Ads Contribution")
    di_amount_ads_created = fields.Date(string="Amount of Ads Created")
    di_amount_ads_contacted = fields.Char(string="Amount Ads Contacted")
    # partner programm matchmacking
    di_date_last_partner_program_contacted = fields.Char(string="Date of the last partner program contacted")
    di_amount_distinct_partner_programs_proact_contacted = fields.Float(
        string="Amount of distinct Partner Programs proactively contacted")
    di_list_partner_program_contacted = fields.Char(string="List of Partner Programs contacted")
    # investor matchmaking
    di_date_last_investor_unlocked = fields.Date(string="Date of the last Investor unlocked")
    di_date_last_investor_contacted = fields.Date(string="Date of the last Investor contacted")
    di_amount_investor_unclocked = fields.Char(string="Amount of Investors unlocked")
    di_amount_distinct_invertor_programs_proact_contacted = fields.Char(
        string="Amount of distinct Investors proactively contacted")
    di_list_investor_contacted = fields.Char(string="List of Investor contacted")

    # company
    company_lega_name = fields.Char(string="Company Lega Name")
    di_company_lega_name = fields.Char(string="Company Lega Name")
    hq_email = fields.Char(string="HQ Email")
    di_hq_email = fields.Char(string="HQ Email")
    horizontal_ids = fields.Many2many('devinsider.horizontal', string="Horizontal")
    di_horizontal = fields.Char(string="Horizontal")
    vertical_ids = fields.Many2many('devinsider.vertical', string="Vertical")
    di_vertical = fields.Char(string="Vertical")
    founded = fields.Char(string="Founded")
    di_founded = fields.Char(string="Founded")
    comp_company_type = fields.Char(string="Company Type")
    contry = fields.Char(string="Contry(ies)")
    comapany_size = fields.Char(string="Company Size")
    di_comapany_size = fields.Char(string="Company Size")
    pre_listed_comp_page_devinsider = fields.Char(string="Pre-listed Company Page on Devinsider")
    active_comp_page = fields.Char(string="Active Company Page (Created or Claimed Ownership)")

    phone_1 = fields.Char(string="Phone")
    email_1 = fields.Char(string="Email")

    street_2 = fields.Char()
    street2_2 = fields.Char()
    zip_2 = fields.Char(change_default=True)
    city_2 = fields.Char()
    state_id_2 = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                                 domain="[('country_id', '=?', country_id)]")
    country_id_2 = fields.Many2one('res.country', string='Country', ondelete='restrict')
    phone_2 = fields.Char(string="Phone")
    email_2 = fields.Char(string="Email")

    street_3 = fields.Char()
    street2_3 = fields.Char()
    zip_3 = fields.Char(change_default=True)
    city_3 = fields.Char()
    state_id_3 = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                                 domain="[('country_id', '=?', country_id)]")
    country_id_3 = fields.Many2one('res.country', string='Country', ondelete='restrict')
    phone_3 = fields.Char(string="Phone")  # mbola ts napotra
    email_3 = fields.Char(string="Email")

    # Financials
    annual_turnover = fields.Char(string="Annual Turnover")
    annual_turnover_bracket = fields.Char(string="Annual Turnover Bracket")
    looking_funding = fields.Char(string="Looking for funding?")
    amount_targeted = fields.Char(string="Amount targeted")
    di_amount_targeted = fields.Char(string="Amount targeted")
    number_funding_round = fields.Integer(string="Number of Funding Round")
    last_funding_date = fields.Date(string="Last Funding Date")
    di_last_funding_date = fields.Date(string="Last Funding Date")
    total_funding_amount = fields.Char(string="Total Funding Amount")

    # Strategy
    licensing_model = fields.Char(string="Licensing Model")
    di_licensing_model = fields.Char(string="Licensing Model")
    distribution_channel = fields.Char(string="Distribution channel")
    di_distribution_channel = fields.Char(string="Distribution channel")
    number_product = fields.Char(string="Number of product")
    technology_partnership = fields.Char(string="Technology Partnership")
    technology_partnership_place = fields.Char(string="Technology partnerships in place")
    di_technology_partnership_place = fields.Char(string="Technology partnerships in place")

    # social media
    linkedin = fields.Char(string="LinkedIn")
    twitter = fields.Char(string="Twitter")
    facebook = fields.Char(string="Facebook")

    # mirror company
    di_company_name = fields.Char(string="Company name")
    di_website = fields.Char(string="Website")
    di_heasquarter_location = fields.Char(string="Headquarter Location")
    di_company_summary = fields.Char(string="Company Summary")
    di_amount_team = fields.Char(string="Amount of Team")
    di_members = fields.Char(string="Members")
    di_geo_target_market = fields.Char(string="Geo. Target Market")
    di_product_development = fields.Char(string="product Development")
    di_expansion_strategy = fields.Char(string="Expansion Strategy")
    di_technology_partnership_interest = fields.Char(string="Technology Partnership interests")
    di_annual_turnover_chart = fields.Char(string="Annual Turnover Chart")

    # pitch
    di_paint_point_solving = fields.Char(string="What Paint Point are you solving?")
    di_key_competitive_differentiator = fields.Char(string="What are your key competitive differentiator?")
    di_make_team_uniques = fields.Char(string="What Makes your team unique")
    devinsider_pitch = fields.Char(string="Devinsider Pitch")

    # contact information mirror company
    di_pre_listed_comp_page_devinsider = fields.Char(string="Pre-listed Company Page on Devinsider")

    #Company page engagement mirror
    di_last_modif_date = fields.Date(string="Last Modified Date")
    di_company_page_compl_prog_matchmaking = fields.Char(string="Company Page completed for Programs Matchmaking")
    di_company_page_compl_invest_matchmaking = fields.Char(string="Company page completed for Investor Matchmaking")
    di_devinsider_pitch_published = fields.Char(string="Devinsider pitch published")


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
