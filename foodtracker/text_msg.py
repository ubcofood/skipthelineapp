import vonage

client = vonage.Client(key="9c078ac5", secret="yG3X7zVc8Zgr8ra7")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "12266200405",
        "to": "12508637975",
        "text": "Your Order#1001 has been confirmed!",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
