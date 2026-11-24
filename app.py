from flask import Flask, request
import requests
import os

app = Flask(__name__)

# YAHAN APNA TOKEN AUR ID DALO
TOKEN = "APNA_TEMPORARY_TOKEN_YAHAN_DALO"
PHONE_ID = "APNA_PHONE_NUMBER_ID_YAHAN_DALO"
VERIFY_TOKEN = "sheebi123"

def send_message(to, text):
    url = f"https://graph.facebook.com/v18.0/{PHONE_ID}/messages"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    data = {"messaging_product": "whatsapp", "to": to, "type": "text", "text": {"body": text}}
    requests.post(url, headers=headers, json=data)

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    try:
        msg = data['entry'][0]['changes'][0]['value']['messages'][0]
        from_no = msg['from']
        user_text = msg['text']['body'].strip()

        if user_text.lower() in ["hi", "hello", "salam", "assalam"]:
            reply = "Assalam-o-Alaikum! Welcome to Sheebi Canteen 😊\n\n1. Menu\n2. Order Karna Hai\n3. Price Puchna Hai\n4. Timing / Location\n\n1, 2, 3 ya 4 likhein"
        
        elif user_text == "1":
            reply = "Sheebi Canteen - Menu 😋\n\n1. Cigarettes - Different Price\n2. Cold Drinks - Different Price\n3. Samosa\n4. Roll\n5. Biscuits\n6. Anda Shami Burger\n7. Chai (Tea)\n\nOrder ke liye 2 likhein"
        
        elif user_text == "2":
            reply = "Zabardast! 😊\nOrder ke liye ye bhej dein:\n\n1. Item + Kitna?\n2. Apna Naam\n\nExample: 1 Chai + 1 Samosa, Ali"
        
        elif user_text == "3":
            reply = "Kon si cheez ka price chahiye?\nCigarette ka naam ya Cold Drink ka naam likh dein, main price bata dunga. 😊"
        
        elif user_text == "4":
            reply = "Sheebi Canteen\nTiming: 06:00 AM - 12:30 AM\nLocation: Opposite Of Giggle World\nRoz khula hai 😊"
        
        else:
            reply = "Shukriya! 😊\nOrder ke liye 2 likhein, Menu ke liye 1 likhein.\nPayment JazzCash Till ID: 984803251"

        send_message(from_no, reply)
    except:
        pass
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
