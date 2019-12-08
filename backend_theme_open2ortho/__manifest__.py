# -*- coding: utf-8 -*-
# Copyright 2016, 2019 Openworx
# Copyright 2019 Open2Bizz
# Based on the Material Backend Theme from Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Open2Ortho backend Theme V12",
    "summary": "Open2Ortho backend Theme V12",
    "version": "12.0.0.1",
    "category": "Theme/Backend",
    "website": "http://www.open2ortho.eu",
	"description": """
		Backend theme for Open2Ortho 12.0.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Open2Bizz, Openworx",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',

    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
		'views/users.xml',
        'views/sidebar.xml',
		#'views/web.xml',
    ],

}

