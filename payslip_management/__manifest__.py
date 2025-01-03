{
    'name': "Pay Slip",
    'category':"Odoo Simple Employee Payslip",
    'summary': """
        HR module customization,removing filed,updating data and new flow   
    """,

    'description': """
       HR Customization 
    """,

    'author': "Pann Phyu",
    'website': "http://www.yourcompany.com",
    'license':'LGPL-3',
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employee_payslip_view_form.xml',
    ],
    # only loaded in demonstration mode
    'application': True,
    'installable': True,
}
