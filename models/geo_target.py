# -*- coding: utf-8 -*-


from odoo import models, fields


class GeoTargetCounty(models.Model):
    _name = 'devinsider_api.geo_target_country'

    name = fields.Char('Name')


class GeoTargetCity(models.Model):
    _name = 'devinsider_api.geo_target_city'

    name = fields.Char('Name')
    country_id = fields.Many2one('devinsider.geo_target_country', string='Country')