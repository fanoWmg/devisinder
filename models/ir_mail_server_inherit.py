# -*- coding: utf-8 -*-


from odoo import models, fields, api


class IrMailServerInherit(models.Model):
     _inherit = 'ir.mail_server'

     is_devinsider_out_going = fields.Boolean("Devinsider API mail out going")

