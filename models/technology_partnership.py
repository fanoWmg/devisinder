# -*- coding: utf-8 -*-


from odoo import models, fields


class TechnologyPartnership(models.Model):
    _name = 'devinsider_api.technology_partnership'

    name = fields.Char('Name')


class TechnologyPartnershipLine(models.Model):
    _name = 'devinsider_api.technology_partnership_line'

    name = fields.Char('Name')
    techno_id = fields.Many2one('devinsider_api.technology_partnership', string='Country')