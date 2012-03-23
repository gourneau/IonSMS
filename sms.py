from twilio.rest import TwilioRestClient

account = "ACd5414a41b5e04399a54ebed8c8564782"
token = "8b6ede860a3390b0cb75d6d6c73f92a4"
client = TwilioRestClient(account, token)

import sys

report =  sys.argv[1]

message = client.sms.messages.create(to="+16153975338", from_="(415) 599-2671", body=report)
