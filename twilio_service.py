import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone = os.environ["TWILIO_PHONE"]
my_phone = os.environ["MY_PHONE"]


def send_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                    body=message,
                    from_= twilio_phone,
                    to= my_phone
                    )
        

    print(message.status)