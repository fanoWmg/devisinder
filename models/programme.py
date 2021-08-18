#-*- coding: utf-8 -*-

from odoo import models, fields, api


class DevinsiderProgramme(models.Model):
    _name = 'devinsider_api.programme'

    name = fields.Char(string="Programme")