# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    po_first_name = fields.Char(string="First name")
    po_last_name = fields.Char(string="Last name")
    address = fields.Char(string="Address")
    # email_score = fields.Char(string="Email Score")
    email_hard_bounced = fields.Boolean(string="Email Hard Bounced")
    email_soft_bounced = fields.Boolean(string="Email Soft Bounced")
    email_pro = fields.Char(string="Email", readonly=True)
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
    di_contact_status = fields.Char(string='Contact Status', readonly=True)

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

    # primary info
    # = fields.Boolean(string="Newsletter for isvs")
    # pri_news_letter_for_isvs = fields.Boolean(string="Newsletter for isvs")

    ###### DI Mirror ######
    id_di_mirror = fields.Char(string='Mirror indentification')
    di_name = fields.Char(string='Name')
    di_email_pro = fields.Char(string='Email')
    di_fistname = fields.Char(string='First Name')
    di_lastname = fields.Char(string='Last Name')
    # di_image_profil = fields.Binary(string='.', readonly=True)
    di_job_position = fields.Char(string='Job position', readonly=True)
    di_city = fields.Char(string='City', readonly=True)
    di_country_id = fields.Many2one('res.country', 'Country', readonly=True)
    di_primary_email = fields.Char(string='Primary Email', readonly=True)
    di_work_email = fields.Char(string='Work Email', readonly=True)
    di_phone = fields.Char(string='Phone', readonly=True)
    di_linkedin = fields.Char(string='Linkedin', readonly=True)
    di_about = fields.Text(string='About', readonly=True)

    di_email_score = fields.Char(string="Email score")
    di_email_hard_bounced = fields.Boolean(string="Email Hard Bounced")
    di_email_soft_bounced = fields.Boolean(string="Email Soft Bounced")
    # Profil overview
    di_first_name_po = fields.Char(string="First Name", readonly=True)
    di_last_name_po = fields.Char(string="Last Name", readonly=True)
    di_job_location = fields.Char(string="Location", readonly=True)

    di_contact_category = fields.Selection([
        ('software_vendor', 'Software Vendor'),
        ('reseller', 'Reseller'),
        ('gest', 'Gest'),
        ('expert_contributor', 'Expert Contributor'),
        ('institutional_investor', 'Institutional Investor'),
        ('individual_investor', 'Individual Investor'),
        ('partner_program', 'Partner Program'),
    ], string='Contact Category')
    di_contact_status = fields.Char(string="Contact Status")
    di_date_signup = fields.Date(string="Date of Sign-Up", readonly=True)
    di_date_last_login = fields.Date(string="Date of the last Log-In", readonly=True)
    di_active_company_page = fields.Boolean(string="Active Company Page (Created, affiliated or Claimed Ownership)",
                                            readonly=True)
    di_date_creation_claimed_own = fields.Date(string="Date of Creation/Claimed Ownership", readonly=True)
    # Mirror Comminity
    di_discussion_categ_followed = fields.Char(string="Discussion Categorie Followed", readonly=True)
    di_label_followed = fields.Char(string="Label Followed", readonly=True)
    di_date_last_forum_contrib = fields.Char(string="Date of the last Forum Contribution", readonly=True)
    di_amount_forum_created = fields.Float(string="Amount of Forum Created", readonly=True)
    di_amount_forum_replie = fields.Float(string="Amount of Forum replies", readonly=True)
    di_amount_replie_qualified_best_answer = fields.Float(string='Amount of replies qualified as "Best Answer"',
                                                          readonly=True)
    di_date_last_article_contrib = fields.Char(string="Date of the last Article Contributions", readonly=True)
    di_amount_article_created = fields.Char(string="Amount of article Created", readonly=True)
    di_date_last_pres_realese_contrib = fields.Char(string="Date of the Last Press Release Contribution", readonly=True)
    di_amount_press_release_created = fields.Char(string="Amount of Press Releases Created", readonly=True)
    di_date_last_programme_reviews_contrib = fields.Char(string="Date of the last Program Reviews Contributions",
                                                         readonly=True)
    di_amount_programme_reviews = fields.Char(string="Amount of Program Review Created", readonly=True)
    di_community_profil_description = fields.Char(string="Community Profil Description", readonly=True)
    # Classified Ads
    di_date_last_ads_contrib = fields.Date(string="Date of Last Ads Contribution", readonly=True)
    di_amount_ads_created = fields.Float(string="Amount of Ads Created", readonly=True)
    di_amount_ads_contacted = fields.Char(string="Amount of Ads Contacted", readonly=True)
    # partner programm matchmacking
    di_date_last_partner_program_contacted = fields.Char(string="Date of the last partner program contacted",
                                                         readonly=True)
    di_amount_distinct_partner_programs_proact_contacted = fields.Float(
        string="Amount of distinct Partner Programs proactively contacted", readonly=True)
    di_list_partner_program_contacted = fields.Char(string="List of Partner Programs contacted", readonly=True)
    # investor matchmaking
    di_date_last_investor_unlocked = fields.Date(string="Date of the last Investor unlocked", readonly=True)
    di_date_last_investor_contacted = fields.Date(string="Date of the last Investor contacted", readonly=True)
    di_amount_investor_unclocked = fields.Char(string="Amount of Investors unlocked", readonly=True)
    di_amount_distinct_invertor_programs_proact_contacted = fields.Char(
        string="Amount of distinct Investors proactively contacted", readonly=True)
    di_list_investor_contacted = fields.Char(string="List of Investor contacted", readonly=True)

    # company
    company_lega_name = fields.Char(string="Company Lega Name")
    di_company_lega_name = fields.Char(string="Company Lega Name")
    hq_email = fields.Char(string="HQ Email")
    di_hq_email = fields.Char(string="HQ Email")
    horizontal_ids = fields.Many2many('devinsider.horizontal', string="Horizontal")
    di_horizontal = fields.Char(string="Horizontal", readonly=True)
    vertical_ids = fields.Many2many('devinsider.vertical', string="Vertical")
    di_vertical = fields.Char(string="Vertical", readonly=True)
    founded = fields.Char(string="Founded")
    di_founded = fields.Char(string="Founded", readonly=True)
    comp_company_type = fields.Char(string="Company Type")
    contry = fields.Char(string="Contry(ies)")
    comapany_size = fields.Char(string="Company Size")
    di_comapany_size = fields.Char(string="Company Size", readonly=True)
    pre_listed_comp_page_devinsider = fields.Boolean(string="Pre-listed Company Page on Devinsider")
    active_comp_page = fields.Boolean(string="Active Company Page (Created or Claimed Ownership)")

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
    di_annual_turnover = fields.Char(string="Annual Turnover", readonly=True)
    di_annual_turnover_bracket = fields.Char(string="Annual Turnover Bracket", readonly=True)
    looking_funding = fields.Char(string="Looking for funding?")
    amount_targeted = fields.Monetary(string="Amount targeted")
    di_amount_targeted = fields.Char(string="Amount targeted", readonly=True)
    number_funding_round = fields.Integer(string="Number of Funding Round")
    last_funding_date = fields.Date(string="Last Funding Date")
    di_last_funding_date = fields.Date(string="Last Funding Date", readonly=True)
    total_funding_amount = fields.Monetary(string="Total Funding Amount")

    # Strategy
    licensing_model = fields.Selection(
        [('on_promise', 'On-Promise'), ('sass', 'Sass'), ('hybrid', 'Hybrid'),
         ('embedded_software', 'Embedded Software (OEM)')],
        string="Licensing Model")
    geo_target_market = fields.Many2one('devinsider_api.geo_target_city', string="Geo Target Market")
    di_licensing_model = fields.Char(string="Licensing Model", readonly=True)
    distribution_channel = fields.Selection(
        [('direct_end_user', 'Direct to End-User'), ('sell_through_dealer_network', 'Sell through a Dealer Network'),
         ('sell_through_var', 'Sell through a VAR')],
        string="Distribution channel")
    di_distribution_channel = fields.Char(string="Distribution channel", readonly=True)
    number_product = fields.Char(string="Number of product")
    technology_partnership = fields.Many2one('devinsider_api.technology_partnership_line',
                                             string="Technology Partnership")
    technology_partnership_place = fields.Char(string="Technology partnerships in place")
    di_technology_partnership_place = fields.Char(string="Technology partnerships in place", readonly=True)

    # social media
    linkedin = fields.Char(string="LinkedIn")
    twitter = fields.Char(string="Twitter")
    facebook = fields.Char(string="Facebook")

    # mirror company
    di_company_name = fields.Char(string="Company name")
    di_website = fields.Char(string="Website", readonly=True)
    di_heasquarter_location = fields.Char(string="Headquarter Location", readonly=True)
    di_company_summary = fields.Char(string="Company Summary", readonly=True)
    di_amount_team = fields.Char(string="Amount of Team", readonly=True)
    di_members = fields.Char(string="Members", readonly=True)
    di_geo_target_market = fields.Char(string="Geo. Target Market", readonly=True)
    di_product_development = fields.Char(string="product Development", readonly=True)
    di_expansion_strategy = fields.Char(string="Expansion Strategy", readonly=True)
    di_technology_partnership_interest = fields.Many2one('devinsider_api.technology_partnership_line',
                                                         string="Technology Partnership interests", readonly=True)
    di_annual_turnover_chart = fields.Char(string="Annual Turnover Chart", readonly=True)

    # pitch
    di_paint_point_solving = fields.Char(string="What Paint Point are you solving?", readonly=True)
    di_key_competitive_differentiator = fields.Char(string="What are your key competitive differentiator?",
                                                    readonly=True)
    di_make_team_uniques = fields.Char(string="What Makes your team unique", readonly=True)
    devinsider_pitch = fields.Char(string="Devinsider Pitch", readonly=True)

    # contact information mirror company
    di_pre_listed_comp_page_devinsider = fields.Char(string="Pre-listed Company Page on Devinsider", readonly=True)

    # Company page engagement mirror
    di_last_modif_date = fields.Date(string="Last Modified Date", readonly=True)
    di_company_page_compl_prog_matchmaking = fields.Char(string="Company Page completed for Programs Matchmaking",
                                                         readonly=True)
    di_company_page_compl_invest_matchmaking = fields.Char(string="Company page completed for Investor Matchmaking",
                                                           readonly=True)
    di_devinsider_pitch_published = fields.Char(string="Devinsider pitch published", readonly=True)

    # Classified ads company
    di_contributed_last_30_day = fields.Char(string="Contributed in the last 30 days", readonly=True)
    di_contributed_last_60_day = fields.Char(string="Contributed in the last 60 days", readonly=True)

    # partner programm matchmaking
    di_amount_distinct_partner_prog_contact_isv = fields.Char(
        string="Amount of distinct Partner programs that have contacted this ISV", readonly=True)

    # programme partner
    is_partner_programme = fields.Boolean(string="I a partner programme")
    oem_programme_id = fields.Many2one('devinsider_api.programme', string="Programme")
    oem_affiliated_partner_id = fields.Many2one('res.partner', string="Affiliated Partner")
    oem_program_segment = fields.Char(string='Program Segment')
    di_oem_program_segment = fields.Char(string='Program Segment')
    oem_program_name = fields.Char(string='Program Name')
    di_oem_program_name = fields.Char(string='Program Name')
    oem_program_type = fields.Char(string='Program Type')
    di_oem_program_type = fields.Char(string='Program Type')
    di_oem_date_last_event_published = fields.Char(string='Date Last Event Published')
    di_oem_amount_event_published = fields.Date(string='Amount of event Published')
    di_oem_date_last_ads_contacted = fields.Date(string='Date of Last Ads Contacted')
    di_oem_amount_ads_contacted = fields.Float(string='Amount of Ads Contacted')

    # affiliated Program
    di_amount_affiliated = fields.Float(string="Amount of affiliated programs", readonly=True)
    partner_program_1 = fields.Char(string="Partner Program 1", readonly=True)  # many2one
    partner_program_2 = fields.Char(string="Partner Program 2", readonly=True)  # many2one
    di_oem_uploaded_document = fields.Binary(string="Uploaded Document")

    # rule
    di_primary_info_not_empty = fields.Boolean()

    def get_devinsider_platform_enablement_lists(self):
        try:
            import requests
            url = "https://preprod1.wylog.com/devinsider2-dev/public/api/odoo/enablement_lists"
            res = requests.get(url).json()
            print(res)
        except:
            pass
        self.devinsider_platform_enablement_lists = True

    devinsider_platform_enablement_lists = fields.Boolean(string="Devinsider platform enablement_lists",
                                                          compute="test_compute")
    devinsider_new_promotion_list = fields.Boolean(string="Devinsider New an Promotion Lists")
    devinsider_partner_communication_list = fields.Boolean(string="Devinsider partner Communication Lists")
    devinsider_community_lists = fields.Boolean(string="Devinsider Community Lists")

    # @api.depends('id_from_devinsider')
    # def _get_di_oem_amount_isvs_unlocked(self):
    #     data = devinsider_api_function(id_from_devinsider)
    #     self.di_oem_amount_isvs_unlocked = data

    di_oem_amount_isvs_unlocked = fields.Float(
        string="Amount of ISVs unlocked")  # , compute=_get_di_oem_amount_isvs_unlocked
    di_oem_amount_distinct_isvs_proact_contacted = fields.Float(string="Amount of distinct ISVs proactively contacted")
    di_oem_date_last_isv_contacted = fields.Char(string="Date of last ISV contacted")
    di_oem_distinct_isvs_contacted_part_prog = fields.Char(
        string="Amount of distinct ISVs that have contacted this Partner Program")



    # @api.onchange('first_name', 'last_name')
    # def onchange_first_last_name(self):
    #     if self.first_name or self.last_name:
    #         name_tab = [self.first_name or '', self.last_name or '']
    #         name = ' '.join(name_tab)
    #     else:
    #         name = False
    #     self.name = name

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

    def open_record(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'name': 'Record name',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref('base.view_partner_form').id,
            'res_id': self.id,
            'target': 'current',
        }

    def crud_primary_info(self, vals):
        if vals.get('di_contact_category'):
            vals['contact_category'] = vals.get('di_contact_category')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_contact_status'):
            vals['contact_status'] = vals.get('di_contact_status')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_lastname') and vals.get('di_fistname'):
            vals['last_name'] = vals.get('di_lastname')
            vals['first_name'] = vals.get('di_fistname')
            vals['name'] = vals.get('di_fistname') + " " + vals.get('di_lastname')
            vals['di_name'] = vals.get('di_fistname') + " " + vals.get('di_lastname')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_email_score'):
            vals['email_score'] = vals.get('di_email_score')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_email_hard_bounced'):
            vals['email_hard_bounced'] = vals.get('di_email_hard_bounced')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_email_soft_bounced'):
            vals['email_soft_bounced'] = vals.get('di_email_soft_bounced')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_email_pro'):
            vals['email_pro'] = vals.get('di_email_pro')

        # company
        if vals.get('di_company_name'):
            vals['company_name'] = vals.get('di_company_name')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_company_lega_name'):
            vals['company_lega_name'] = vals.get('di_company_lega_name')
            vals['di_primary_info_not_empty'] = True
        if vals.get('di_hq_email'):
            vals['hq_email'] = vals.get('di_hq_email')
            vals['di_primary_info_not_empty'] = True

    @api.model
    def create(self, vals):
        self.crud_primary_info(vals)
        return super(ResPartnerInherit, self).create(vals)

    def write(self, vals):
        self.crud_primary_info(vals)
        return super(ResPartnerInherit, self).write(vals)

    @api.onchange('di_fistname', 'di_lastname')
    def onchange_mir_name(self):
        if self.di_fistname and self.di_lastname:
            self.first_name = self.di_fistname
            self.last_name = self.di_lastname
            self.name = self.first_name or "" + " " + self.last_name or ""

    @api.onchange('di_name')
    def onchange_di_name(self):
        if self.di_name:
            self.name = self.di_name
