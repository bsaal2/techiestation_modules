# -*- coding: utf-8 -*-
{
    'name': "techiestation",

    'summary': """
        Techiestation is an internet company""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Bishal Giri",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/templates.xml',
        'views/assets.xml',
        'views/category_view.xml',
        'views/menu.xml',
        'views/home.xml',
        'views/mobile.xml',
        'views/tablet.xml',
        'views/laptop.xml',
        'views/camera.xml',
        'views/design.xml',
        'views/detail.xml',
        'views/connect.xml',

        # Backend Views
        'views/posts_view.xml',
    ],
}