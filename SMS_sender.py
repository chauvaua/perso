# Installer d'abord la librairie Twilio
# pip install twilio

from twilio.rest import Client

# Remplacer par vos identifiants Twilio
account_sid = 'id'
auth_token = 'REMOVED'
client = Client(account_sid, auth_token)

# Numéros de téléphone
from_number = '+330650665618'  # Numéro Twilio
to_number = '+330780056723'   # Numéro destinataire

message = client.messages.create(
    body="Hello depuis Python !",
    from_=from_number,
    to=to_number
)

print("Message envoyé, SID :", message.sid)
