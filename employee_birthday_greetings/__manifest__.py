# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/

{
    'name': 'Employee Birthday Greetings',
    'category': 'HR',
    'version': '11.0.1.0.0',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Automated system for sending greetings to employee on their birthday.',
    'summary': """
        User can set the Customised email format for there employees.And when 
        the Bigday for employee arrived he/she will receive the Greetings.""",

    'license': "AGPL-3",

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
