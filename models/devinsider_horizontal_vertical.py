# -*- coding: utf-8 -*-

from odoo import models, fields


class Horizontale(models.Model):
    _name = 'devinsider.horizontal'

    name = fields.Char(string="Name")


class Vertical(models.Model):
    _name = 'devinsider.vertical'

    name = fields.Char(string="Name")
