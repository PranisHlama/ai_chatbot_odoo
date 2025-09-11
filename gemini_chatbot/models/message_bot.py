from odoo import models, api
import re, logging
import markdown
from bs4 import BeautifulSoup

_logger = logging.getLogger(__name__)

def strip_markdown(md_text_: str) -> str:
    html = markdown.markdown(md_text_, extensions=['extra'])

    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n\n")
    text = text.strip()
    text = re.sub(r'\n{3,}', '\n\n', text)  # Replace 3+ newlines with 2 newlines
    return text

class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, vals_list):
        _logger.info(f"[GeminiBot] create() called with vals: {vals_list}")

        messages = super().create(vals_list)
        bot_partner = self.env['res.partner'].browse(96)

        for message in messages:
            if message.model == "discuss.channel" and message.res_id:
                channel = self.env["discuss.channel"].browse(message.res_id)
                _logger.info(f"[GeminiBot] New message in channel: {channel.name}, from: {message.author_id.display_name}")

                # Skip bot's own messages
                if bot_partner and message.author_id == bot_partner:
                    _logger.info("[GeminiBot] Skipping own message")
                    continue

                raw_body = message.body or ""
                text = re.sub(r"<[^>]*>", "", raw_body).strip()
                if not text:
                    continue

                _logger.info(f"[GeminiBot] User said: {text}")

                try:
                    reply = self.env["gemini.chatbot.api"].ask_gemini(text)
                    clean_reply = strip_markdown(reply)
                    _logger.info(f"[GeminiBot] Gemini replied: {clean_reply}")

                    channel.message_post(
                        body= clean_reply,
                        message_type="comment",
                        subtype_xmlid="mail.mt_comment",
                        author_id=bot_partner.id,
                    )
                except Exception as e:
                    _logger.error(f"[GeminiBot] Error: {e}")
                    channel.message_post(
                        body="Sorry, I am having trouble connecting to Gemini service right now.",
                        message_type="comment",
                        subtype_xmlid="mail.mt_comment",
                    )

        return messages

