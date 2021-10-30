import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random # generate random number
otp = random.randint(1000,9999)
print("Your OTP is - ",otp)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC96007a43e6330a1ac90a6a888455d9aa'
auth_token = '8289b60896e4da3840e4c021e35dc136'
client = Client(account_sid, auth_token)

message = client.messages.create(body='Hello Mr. Mayur Your Secure Device OTP is - ' + str(otp) + 'now your mobile is hacked!\n Byby...',from_='+13203001186',to='+919019375543')

print(message.sid)
