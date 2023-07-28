# -*- coding: utf-8 -*-
{
    'name': "Notification",
    'author': "Sneha",
    'version': '0.1',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_data.xml',
        'views/celebration_views.xml',
        'views/template_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
