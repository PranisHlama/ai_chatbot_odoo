from odoo import SUPERUSER_ID
from odoo.api import Environment

def create_chatbot_dm(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    chatbot_user = env.ref("gemini_chatbot.gemini_chatbot_chatbot_user", raise_if_not_found=False)

    if chatbot_user:
        chatbot_partner = chatbot_user.partner_id
        for user in env["res.users"].search([]):
            if user.id == chatbot_user.id:
                continue
        
        env["mail.channel"].create({
            "name": "Chat with Gemini Chatbot",
            "channel_type": "chat",
            "channel_partner_ids": [(6, 0, [user.partner_id.id, chatbot_partner.id])],
        })