from odoo import models, views, api
import os

api_key = os.getenv("GEMINI_API_KEY")

class AIChatbotMain(models.Model):
    _name = 'ai.chatbot.main'
    _description = 'AI Chatbot Main Model'
    
    