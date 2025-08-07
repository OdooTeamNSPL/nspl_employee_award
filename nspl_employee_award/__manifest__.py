{
    'name': 'Employee Award Management',
    'version': '16.0',
    'summary':
        """
    The Employee Award Management app in Odoo Simplifies tracking and managing employee awards with detailed records, reporting, and print-ready documentation.
    """,

    'description': """
    ✔ Record employee awards with type, granting authority, and winning amount  
    ✔ Easily generate and print comprehensive award reports  
    ✔ Maintain a clear historical archive of all employee awards  
    ✔ Promote a culture of recognition and motivation in the organization  

    This module helps HR and management efficiently track and manage employee awards. With well-structured forms and printable reports, it enhances transparency and simplifies recognition processes across the company.""",

    'category': 'Employee',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com/',
    'license': 'OPL-1',
    'price': 14.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['hr', 'mail', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/award_type.xml',
        'views/employee_award_views.xml',
        'views/award_page.xml',
        'report/employee_award_report_action.xml',
        'report/employee_award_report_template.xml',

    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
