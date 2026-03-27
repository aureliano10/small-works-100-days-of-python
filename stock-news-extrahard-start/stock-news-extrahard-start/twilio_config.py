from dotenv import load_dotenv
import os
from  twilio.rest  import  Client
load_dotenv()

account_sid  = os.environ.get("TWILIO_ACCOUNT_SID")
token_autenticacion  = os.environ.get("TWILIO_TOKEN_AUTH")

client  =  Client(account_sid, token_autenticacion)

def info_msj(title, new):
    message = client.messages.create(
        body=f"{title}\n"
             f"{new}",
        from_="+14786063927",
        to="+543533686671",
    )
    print(message.sid)

def first_msj(variation):
    message = client.messages.create(
        body=f"Tus acciones en Tesla variaron un %{variation}",
        from_="+14786063927",
        to="+543533686671",
    )
    print(message.sid)

