# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response

import json

# test en dev
DB = "crm"
LOGIN = "arthur@mediadev.com"
PSWD = "Qwerty789"


# test local
#DB = "devisinder"
#LOGIN = "admin"
#PSWD = "admin1234"


class MirrorController(http.Controller):

    @http.route('/devinsider_api/mirror', auth='public', type='json')
    def mirror(self, **kw):
        request.session.authenticate(DB, LOGIN, PSWD)
