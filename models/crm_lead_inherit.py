# -*- coding: utf-8 -*-


from odoo import models, fields, api


class CrmLeadInherit(models.Model):
     _inherit = 'crm.lead'

     is_devinsider_lead = fields.Boolean(string="devinside lead")


