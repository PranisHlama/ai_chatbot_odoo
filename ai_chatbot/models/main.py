from odoo import models
from odoo.tools import html2plaintext
import logging

_logger = logging.getLogger(__name__)

class DiscussChannel(models.Model):
    _inherit = 'discuss.channel'
    _description = 'Add chatbot functionality to discuss channels'
    
    def _notify_thread(self, message, msg_vals=False, **kwargs):
        res = super(DiscussChannel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)

        chatbot_user = self.env.ref('gemini_chatbot.gemini_chatbot_chatbot_user', raise_if_not_found=False)
        _logger.info(f"Chatbot user: {chatbot_user}")

        if not chatbot_user or not chatbot_user.partner_id:
            return res
        
        # Avoid infinite loop (ignore chatbot’s own messages)
        if message.author_id and message.author_id == chatbot_user.partner_id:
            _logger.info("Ignoring message from the chatbot to prevent infinite loop.")
            return res
        
        # Detect messages
        if message.message_type == 'comment' and message.body and chatbot_user.partner_id in self.channel_partner_ids:
            text = html2plaintext(message.body).strip()
            _logger.info(f"Message for chatbot detected: {text}")
            
            if f"@{chatbot_user.partner_id.name}" in text or (len(self.channel_partner_ids) == 2):
                _logger.info("Handling chatbot message")
                self.handle_chatbot_message(message, chatbot_user)
        return res
    
    def handle_chatbot_message(self, message, chatbot_user):
        text = html2plaintext(message.body).strip().lower()

        responses = {
            "hello": "Hello! How can I help you today?",
            "hi": "Hello, how are you? 😊",   # <--- Updated reply
            "bye": "Goodbye! Have a nice day.",
            "thanks": "You're welcome! 😊",
        }
        response_text = "I'm not sure I understand. Can you rephrase?"
        for keyword, reply in responses.items():
            if keyword in text:
                response_text = reply
                break

        _logger.info(f"Generating response for message: {text}")

        # Post the response as chatbot partner
        self.message_post(
            body=response_text,
            author_id=chatbot_user.partner_id.id,  # fixed
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
