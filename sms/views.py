from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from twilio.rest.api.v2010 import account

# Create your views here.


account = 'ACXXXXXXXXXXXXXXXXX'  # enter your twilio ACCOUNT SID
token = 'YYYYYYYYYYYYYYYYYY'  # enter your twilio AUTH TOKEN
client = Client(account, token)


def index(request):
    message_to_broadcast = ("Have you played the incredible TwilioQuest "
                            "yet? Grab it here: https://www.twilio.com/quest")
                            
    # You can use the line below to import the accaunt and token from settings and venv
    #client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # or use the line from the top for client credentials

    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)
