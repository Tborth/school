{
    'name': 'Student',
    'version': '1',
    
    'sequence': 12,
    'summary': 'Centralize employee information',
    'description': """
        This module contains all the common features of Sales Management and eCommerce.
    """,
        'depends': [
        'mail',
         'web',
 
    ],
    'data': [
       
    'security/ir.model.access.csv',
    'views/student_models.xml',
    ],
    'demo': [
      
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
