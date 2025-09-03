# 🚀 Quick Start Guide - AI Chat Bot

## **Your Setup is Almost Ready!**

You have your Gemini API key configured in VS Code launch.json, which is perfect for security. Here's how to get your bot running:

## **Option 1: Run Through VS Code (Recommended)**

1. **Open VS Code** and go to the Debug panel (Ctrl+Shift+D)
2. **Select "Odoo 18: Run & Debug"** configuration
3. **Click the green play button** to start Odoo
4. Your bot will automatically have access to the Gemini API key!

## **Option 2: Set Environment Variable**

If you want to run Odoo from terminal:

```bash
export GEMINI_API_KEY="AIzaSyBuEHYx6hdO62waX2avz4m47gVczmRptFM"
```

## **Quick Test**

Run this to verify everything works:

```bash
cd custom/chatgpt_int
python config.py
```

## **Start Your Bot**

1. **Restart Odoo** (through VS Code debugger or terminal)
2. **Go to Discuss → AI Chat Bots → Chat Bots**
3. **Create a new bot** with these settings:

   - Name: "My AI Assistant"
   - System Prompt: "You are a helpful AI assistant in Odoo discussions"
   - Keywords: "help, question, how, what"
   - Auto Respond: ✅ Enabled

4. **Create bot configuration**:
   - Model: `mail.thread`
   - Enable Context: ✅ Yes

## **Test Your Bot**

1. Go to any discussion thread
2. Send a message like: "Can you help me?"
3. Watch your AI bot respond automatically! 🤖

## **Troubleshooting**

- **API Key Error**: Make sure you're running through VS Code debugger
- **Bot Not Responding**: Check if bot is active and configured correctly
- **Module Not Found**: Restart Odoo after installing the module

## **Need Help?**

Run the setup script:

```bash
./setup.sh
```

Your bot is configured and ready to go! 🎉
