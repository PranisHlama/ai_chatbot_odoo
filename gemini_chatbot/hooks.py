from odoo import api, SUPERUSER_ID

def create_discuss_channel(env):
    """Create a new Discuss channel after module installation"""

    channel_name = "Gemini"

    # Check if channel exists
    existing_channel = env['discuss.channel'].search([('name', '=', channel_name)], limit=1)
    if existing_channel:
        return

    # Create channel
    channel = env['discuss.channel'].create({
        'name': channel_name,
        'channel_type': 'channel',
        'description': 'Gemini Chatbot Channel',
        })

    # Post welcome message
    channel.message_post(
        body="👋 Welcome to Gemini Chatbot Channel! Type 'hello' to start chatting.",
        message_type='comment',
        subtype_xmlid='mail.mt_comment'
    )
