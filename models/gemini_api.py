from odoo import models, api
import os, logging
from google import genai

_logger = logging.getLogger(__name__)


class ChatbotAPI(models.AbstractModel):
    _name = 'gemini.chatbot.api'
    _description = 'Gemini Chatbot API Integration'

    @api.model
    def ask_gemini(self, prompt):
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents= prompt,
            )
            if hasattr(response, 'text') and response.text:
                return response.text
            else:
                return "Sorry, I couldn't generate a response."
        
        except Exception as e:
            _logger.error(f"Error communicating with Gemini API: {e}")
            return "Sorry, I am having trouble connecting to the Gemini service right now."
        



    
