from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = 'twilio-key'
# Your Auth Token from twilio.com/console
auth_token = 'twilio-token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+905375411781",  # Replace with the recipient's phone number
    from_="+13203810960",  # Replace with your Twilio phone number
    body=f"")

print(f"Message sent with SID: {message.sid}")
