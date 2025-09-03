from odoo import models, fields
import os 
import requests
import logging

_logger = logging.getLogger(__name__)


class DiscussChannel(models.Model):
    _inherit = 'discuss.channel'
    _description = 'Add chatbot functionality to discuss channels'

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        """Override notification method to detect messages for chatbot"""
        res = super(DiscussChannel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)

        chatbot_user = self.env.ref('gemini_chatbot.gemini_chatbot_chatbot_user', raise_if_not_found=False)
        _logger.info(f"Chatbot user: {chatbot_user}")

        if not chatbot_user or not chatbot_user.partner_id:
            return res

        if(
            message.message_type == 'comment' and
            chatbot_user and
            message.body and
            message.author_id and
            message.author_id != chatbot_user.partner_id and
            chatbot_user.partner_id in self.channel_partner_ids
        ):
            _logger.info(f"Message for chatbot detected: {message.body}")
            if(
                f"@{chatbot_user.partner_id.name}" in message.body or 
                (len(self.channel_partner_ids) == 2 and chatbot_user.partner_id in self.channel_partner_ids)
            ):
                _logger.info("Handling chatbot message")
                self.handle_chatbot_message(message, chatbot_user)
        return res
    
    def handle_chatbot_message(self, message, chatbot_user):
        response_text = "Hi, I am a chatbot. How can I assist you?"
        _logger.info(f"Generating response for message: {message.body}")
        self.message_post(
            body=response_text,
            author_id=chatbot_user.id,
            message_type='comment',
            subtype_xmlid='mail.mt_comment'
        )
        return True


class ChatbotAPI:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

    def ask_gemini(self, prompt):
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        headers = {"Content-Type": "application/json"}
        params = {"key": self.api_key}
        data = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }

        response = requests.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()
