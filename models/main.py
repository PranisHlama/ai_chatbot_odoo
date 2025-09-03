from odoo import models, fields, api
from google import genai
import os 
import requests
import logging

_logger = logging.getLogger(__name__)


class DiscussChannel(models.Model):
    _inherit = 'discuss.channel'
    _description = 'Add chatbot functionality to discuss channels'

    chatbot_field = fields.Char(string="New Field")



class ChatbotAPI:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

    def ask_gemini(self, prompt):
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        headers = {"Content-Type": "application/json"}
        params = {"key": "self.api_key"}
        data = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }

        response = requests.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()
        
{
    # has_chatbot = fields.Boolean(string="Enable Chatbot", default=False)
    # chatbot_name = fields.Char(string="Chatbot Name", default="Geminibot")
    # chatbot_prompt = fields.Text(
    #     string="Chatbot Instructions",
    #     default="You are Geminibot, a helpful AI assistant. Be friendly, helpful, and concise."
    # )
    # chatbot_triggers = fields.Char(
    #     string="Trigger Words",
    #     default="bot,help,geminibot",
    #     help="Comma-separated list of words that trigger the chatbot."
    # )
}


{#     def _get_or_create_geminibot_user(self):
#         """Get the existing Geminibot user"""
#         try:
#             user = self.env['res.users'].search([('email', '=', 'gemini@mail.com')], limit=1)

#             if not user:
#                 _logger.error("Geminibot user (gemini@mail.com) not found. Please create this user first.")
#                 return None

#             _logger.info(f"Found existing Geminibot user: {user.name}")
#             return user
#         except Exception as e:
#             _logger.error(f"Error finding Geminibot user: {str(e)}")
#             return None

#     def _add_geminibot_message(self, message_body):
#         """Post a chatbot message into the channel"""
#         try:
#             user = self._get_or_create_geminibot_user()
#             if not user:
#                 _logger.error("Could not create or find Geminibot user")
#                 return False

#             self.message_post(
#                 body=message_body,
#                 author_id=user.id,
#                 message_type='comment',
#                 subtype_xmlid='mail.mt_comment'
#             )
#             return True
#         except Exception as e:
#             _logger.error(f"Error adding Geminibot message: {str(e)}")
#             return False

#     def _process_geminibot_trigger(self, message):
#         """Check if a message should trigger the bot and respond"""
#         try:
#             triggers = [t.strip().lower() for t in (self.chatbot_triggers or "").split(",")]
#             message_text = (message.body or "").lower().strip()

#             # Skip bot's own messages
#             if message.author_id and message.author_id.email == "gemini@mail.com":
#                 return

#             if self.channel_type == 'chat' or self.has_chatbot:
#                 if any(trigger in message_text for trigger in triggers):
#                     response = self._generate_bot_response(message_text)
#                     self._add_geminibot_message(response)

#         except Exception as e:
#             _logger.error(f"Error processing Geminibot trigger: {str(e)}")

#     def _generate_bot_response(self, message_text):
#         """Very simple response generator (placeholder for real AI API call)"""
#         if "hello" in message_text or "hi" in message_text:
#             return f"Hello! I'm {self.chatbot_name}. How can I help you today? 🤖"
#         elif "help" in message_text:
#             return f"I'm {self.chatbot_name}, your assistant. I can help you with questions and provide info.\nJust ask me anything!"
#         elif "geminibot" in message_text:
#             return f"Hi there! I'm {self.chatbot_name}, here to help. What would you like to know?"
#         else:
#             return f"Hi! I'm {self.chatbot_name}. How can I assist you today?"


# class DiscussMessage(models.Model):
#     _inherit = 'mail.message'
#     _description = 'Add chatbot message processing'

#     @api.model
#     def create(self, vals):
#         """Override create to process messages for chatbot responses"""
#         try:
#             message = super(DiscussMessage, self).create(vals)

#             # Only process channel comments
#             if (message.model == 'discuss.channel'
#                 and message.message_type == 'comment'
#                 and message.body
#                 and message.author_id):

#                 channel = self.env['discuss.channel'].browse(message.res_id)
#                 if channel.exists():
#                     # Run bot check
#                     channel._process_geminibot_trigger(message)

#             return message
#         except Exception as e:
#             _logger.error(f"Error in DiscussMessage create: {str(e)}")
#             return super(DiscussMessage, self).create(vals)
}
