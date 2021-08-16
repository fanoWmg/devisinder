# -*- coding: utf-8 -*-

from odoo.http import request


class DevinsiderConnection(object):

    def __init__(self):
        request.session.authenticate("crm", "arthur@mediadev.com", "Qwerty789")