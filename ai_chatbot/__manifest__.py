{
    'name': "AI Chatbot",
    'summary': "Add AI chatbot functionality directly to Odoo discuss channels",
    'description': """
    AI Chatbot for Discuss Channels
    This module adds a simple AI chatbot directly to your Odoo discuss channels.
    """,
    'author': "Pranish Lama",
    'category': 'Discuss',
    'version': '1.0.0',
    'depends': ['base', 'mail', 'mail_bot'],
    'data': [
        # 'data/gemini_bot_data.xml',
        # 'views/views.xml',
    ],
    # 'post_init_hook': 'create_discuss_channel',
    'installable': True,
    'application': False,
    'auto_install': False,
}

