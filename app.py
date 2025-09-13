from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ✅ Function to fetch conversion rate
def fetch_conversion_factor(source, target):
    API_KEY = "be1800cdad19ccd33b05f6f0b1a72769"  # from your dashboard
    url = f"http://api.exchangerate.host/convert?from={source}&to={target}&amount=1&access_key={API_KEY}"
    response = requests.get(url).json()
    if "result" in response and response["result"]:
        return response["result"]  # conversion factor for 1 unit
    else:
        print("⚠️ Error: API call failed:", response)
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "✅ Flask currency converter is running. Use POST requests from Dialogflow."

    data = request.get_json()
    print("📩 Webhook hit!")
    print("Request JSON:", data)

    try:
        # Extract parameters
        source_currency = data['queryResult']['parameters']['unit-currency'][0]['currency']
        amount = data['queryResult']['parameters']['unit-currency'][0]['amount']
        target_currency = data['queryResult']['parameters']['currency-name'][0]

        # Fetch conversion
        cf = fetch_conversion_factor(source_currency, target_currency)
        if cf is None:
            response = {
                'fulfillmentText': "⚠️ Sorry, I couldn’t fetch conversion rates right now."
            }
        else:
            final_amount = round(amount * cf, 2)
            response = {
                'fulfillmentText': f"{amount} {source_currency} is {final_amount} {target_currency}"
            }

    except Exception as e:
        print("⚠️ Exception:", e)
        response = {
            'fulfillmentText': "⚠️ Something went wrong while processing your request."
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
