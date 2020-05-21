from twilio.rest import Client

account_sid = 'ACeb6de2453338f46ce96c4ce92959654d'
auth_token = '9e88c1e464111401b7983fd9f46b7106'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12059227171',
    body='Love from Claire. She can send an SMS message with Python!',
    to='+886926633478'
)

print(message.sid)
