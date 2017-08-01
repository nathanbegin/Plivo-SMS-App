#// Created by Nathan Begin on 28-02-2017
#// nathanbegin@gmail.com
#//  Copyright 2017 ©  All rights reserved.

import plivo
from tkinter import *
from credentials import *

mainwindow=Tk()
mainwindow.title("Plivo SMS App")
mainwindow.iconbitmap(default='Logo.ico')
mainwindow.geometry('500x150')
mainwindow.configure(background='white')

f1=Frame=
f1.pack()

mainwindow.mainloop()















#p = plivo.RestAPI(auth_id, auth_token)

#params = {
#    'src': my_plivo, # Sender's phone number with country code
#    'dst' : my_cell, # Receiver's phone Number with country code
#    'text' : u"Ceci est un test", # Your SMS Text Message - English

#}
#response = p.send_message(params)
