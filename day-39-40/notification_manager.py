import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID_KEY'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["REAL_NUMBER"]
        )

        print(message.sid)