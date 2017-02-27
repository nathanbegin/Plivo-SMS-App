# -*- coding: utf-8 -*-
import plivo

#Initializing PlivoRestApi
auth_id = "MAZDU1MZC1OGM5MGQ1OW"
auth_token = "OTBlNTY5NGVkNTE5NTc1MjE1OTNlMDQ4YWFhZDlk"
p = plivo.RestAPI(auth_id, auth_token)
num_var = '+14502381594'
params = {
    'src': '+14508772018', # Sender's phone number with country code
    'dst' : num_var, # Receiver's phone Number with country code
    'text' : u"Note: You can send SMS text messages to any country using the Message API and set any ‘src’ number except for US and Canadian numbers. In order to send text messages to phones in the US or Canada, you will need to purchase a US or Canadian phone", # Your SMS Text Message - English
    'url' : "http://morning-ocean-4669.herokuapp.com/report/", # The URL to which with the status of the message is sent
    'method' : 'GET' # he method used to call the url
}
response = p.send_message(params)
# Prints the complete response
# print str(response)

# Sample successful output
#(202, {
#   u'message': u'message(s) queued',
#   u'message_uuid': [u'dcfc1510-9260-11e4-b1a4-22000ac693b1'],
#   u'api_id': u'dce8fb42-9260-11e4-b932-22000ac50fac'
#   }
# )

# Print the Message UUID
uuid = str(response[1]['message_uuid'][0])
# print "Message_uuid : %s " % (uuid)

# Output
# Message_uuid : 2d97bbfe-9262-11e4-9bd8-22000afa12b9'

# To get the SMS split units

params1 = {
    'message_uuid': uuid
}

response1 = p.get_message(params1)

# print "Your SMS was split into %s units" % response1[1]['units']

# Output for Japanese
# Your SMS was split into 3 units

# Output for English
# Your SMS was split into 2 units

# Output for French
# Your SMS was split into 5 units