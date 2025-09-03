{
    'name': "Gemini AI Chatbot",
    'summary': "Add AI chatbot functionality directly to Odoo discuss channels",
    'description': """
AI Chatbot for Discuss Channels
===============================

This module adds a simple AI chatbot directly to your Odoo discuss channels.

Features:
- 🤖 Enable chatbot in any discuss channel
- 💬 Bot responds to messages starting with "bot" or containing "help"
- 👤 Customizable bot name and instructions
- 🔧 Simple integration - no separate bot management needed

Usage:
1. Go to any discuss channel
2. Enable chatbot in channel settings
3. Type "bot hello" or "help" to interact with the bot
4. The bot will respond as another user in the channel
    """,

    'author': "Pranish Lama",
    'category': 'Discuss',
    'version': '1.0.0',
    'depends': ['base', 'mail'],

    'data': [
        'data/chatbot_data.xml',
        'views/views.xml',
    ],
    'post_init_hook': 'create_chatbot_dm',
    
    'installable': True,
    'application': False,
    'auto_install': False,
}

