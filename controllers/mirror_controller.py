# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
from . import main
import logging

_logger = logging.getLogger(__name__)


class MirrorController(http.Controller):

    @http.route('/devinsider_api/mirror', auth='public', type='json')
    def mirror(self, **post):
        main.DevinsiderConnection.__init__(main)
        res_partner_mir = request.env['res.partner']

        try:
            di_name = [post['di_fistname'] or '', post['di_lastname'] or '']
            post['name'] = ' '.join(di_name)
            res_partner_mir.sudo().create(post)
            _logger.info("create partner %r", post)
        except Exception as e:
            _logger.info("create partner %r", e)
        return {
            'status': 'status',
            'message': 'all_message'
        }

    def merge_first_last_name(self):
        name = self.name
        if self.company_type == 'person':
            if self.first_name or self.last_name:
                name_tab = [self.first_name or '', self.last_name or '']
                name = ' '.join(name_tab)
            else:
                name = False
        self.name = name




