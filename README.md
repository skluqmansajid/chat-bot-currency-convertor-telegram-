# 💱 Chat-Bot Currency Converter (Telegram)

A conversational Telegram bot that converts currencies in real-time. Built with **Python, Flask, and Dialogflow**, it fetches live exchange rates from an API and works directly on Telegram.

---

## Step-by-Step Guide

### **1. Create and Train Dialogflow Agent**
1. Go to [Dialogflow ES](https://dialogflow.cloud.google.com/) and **create a new agent**.  
2. Name your agent (e.g., `CurrencyConverterBot`) and select your **default language and timezone**.  
3. **Create Intents**:  
   - Example: `ConvertCurrency`  
   - Add **Training Phrases** users might type:
     ```
     Convert 100 USD to INR
     How much is 50 EUR in GBP?
     ```
   - Add **Parameters**:
     - `unit-currency` (type: `@sys.unit-currency`)
     - `currency-name` (type: `@sys.currency`)  
   - Set **Responses** temporarily; the final response will be from your Flask webhook.

4. **Enable Fulfillment** for the intent:
   - Turn on **Webhook call for this intent**.

---

### **2. Connect Flask Backend**
1. Your `app.py` handles the webhook from Dialogflow:
   - Receives JSON requests with user input.
   - Extracts `source currency`, `target currency`, and `amount`.
   - Calls the **Exchange Rate API** to get the conversion factor.
   - Returns a JSON response back to Dialogflow.
2. Make sure your `app.py` is running:


####  **3. Hosting Locally via Ngrok

1. Install Ngrok: https://ngrok.com/
2. Start Ngrok to expose your local Flask server: ngrok http 5000
3 . Copy the Ngrok HTTPS URL (e.g., https://1234abcd.ngrok.io) — this will be used as your webhook URL.


### **Step 4, 5, 6: Host Flask, Connect Dialogflow & Telegram Bot**


# 4️⃣ Run Flask backend & start Ngrok
python app.py
ngrok http 5000
# Copy the HTTPS URL shown by Ngrok (e.g., https://1234abcd.ngrok.io)

# 5️⃣ Connect Dialogflow webhook
# Go to Dialogflow Console → Fulfillment → Webhook
# Enable Webhook and set the URL:
# https://1234abcd.ngrok.io/
# Save changes
# Test in Dialogflow “Try it now” panel

# 6️⃣ Set Telegram webhook & test
# Create a Telegram bot via @BotFather (if not already done) and get the Bot Token
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=<YOUR_NGROK_URL>"
# Open Telegram and send a message like:
# "Convert 100 USD to INR"
# You should receive a real-time conversion reply
