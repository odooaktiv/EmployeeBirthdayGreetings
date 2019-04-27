# -*- coding: utf-8 -*-

{
    'name': 'Employee Birthday Mail',
    'category': 'HR',
    'version': '11.0.1.0.0',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Schedular for sending email to employee on their birthday.',

    'depends': [
        'mail', 'hr'
    ],

    'data': [
        "data/employee_birthday_email_template.xml",
        'data/birthday_mail_scheduler.xml',
        'views/res_company_view.xml',
        'views/res_users_view.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'auto_install': False,
    'installable': True,
    'application': False

}
