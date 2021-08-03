# -*- coding: utf-8 -*-
{
    'name': "devinsider_api",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'web', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/type_mail_devinsider.xml',
        'views/ir_mail_server_view_inherit.xml',
        #'views/res_partner.xml',
        'views/css_js_loader.xml',
        'views/res_partner_view_inherit.xml',

        'data/template_mail_create_compte.xml',
        'data/action_send_mail_data.xml',
        'data/template_mail_reset_pswd.xml',
        'data/template_mail_verified_pro.xml',
        'data/template_mail_update_mail.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
