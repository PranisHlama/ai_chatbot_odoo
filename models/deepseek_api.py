from odoo import api, models
import os, logging
from openai import OpenAI

_logger = logging.getLogger(__name__)

class DeepseekChatAPI(models.AbstractModel):
    _name = 'deepseek.chatbot.api'
    _description = 'Deepseek Chatbot API Integration'

    @api.model
    def ask_deepseek(self, prompy):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
        
        try:
            client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": prompy},
                ],
                stream=False
            )
            if response and response.choices and len(response.choices) > 0:
                return response.choices[0].message.content
            else:
                return "Sorry, I couldn't generate a response."
        
        except Exception as e:
            _logger.error(f"Error communicating with Deepseek API: {e}")
            return "Sorry, I am having trouble connecting to the Deepseek service right now."
