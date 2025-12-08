{
    'name': 'Therapist Fields for HR',
    'version': '18.0',
    'category': 'Human Resources',
    'summary': 'Therapist Information to be stored.',
    'author': 'Pranish Lama',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/therapist_information.xml',
        'views/hr_config_menu.xml',
        'views/therapist_information_views.xml',
    ],
    'installable': True,
    'application': False,
}