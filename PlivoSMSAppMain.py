#// Created by Nathan Begin on 28-02-2017
#// nathanbegin@gmail.com
#//  Copyright 2017 ©  All rights reserved.
# -*- coding: utf-8 -*-
import plivo
from credentials import *
from message import *

#Initializing PlivoRestApi
p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': my_plivo, # Sender's phone number with country code
    'dst' : my_cell, # Receiver's phone Number with country code
    'text' : mytext,# Your SMS Text Message - English

}
response = p.send_message(params)