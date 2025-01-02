{
    'name': 'Ferry Management Module',
    'version': '1.1',
    'category': 'Ferry/Ferry',
    'summary': 'Ferry Management',
    'author': 'Pann Phyu',
    'description': """
    This module contains the management of ferry.
    """,
    'depends':  ['base','hr','mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/ferry_management_access_rule.xml',
        'data/employee_id_seq.xml',
        'views/kis_ferry_view.xml',
        'views/kis_ferry_management_view.xml',
        'views/menu_item.xml',
    ],

    'installable': True,
    'auto_install': False
}
