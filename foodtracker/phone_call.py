from twilio.rest import Client

sid="AC71ec9f437f59e5d5a3091916a0b61491"
auth_token ="01add7300b37eb3851041c9b99a6addc"

client = Client(sid, auth_token)

resp = client.calls.create(twiml="<Response><Say> Your order number 1001 has been confirmed</Say></Response>", from_="+13853965618", to="+12508637975")

print(resp.sid)