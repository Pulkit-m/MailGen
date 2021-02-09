import os
#using the smtplib library in python: SMTP: Simple Mail Transfer Protocol
import smtplib

sender = os.getenv("EMAIL")
recievers = ['parwaanvirk@gmail.com','pulkitmahajan0402@gmail.com']

message = """From: <2019ucs0073@iitjammu.ac.in>
To: To Person <2019ume0203@iitjammu.ac.in>
Subject: SMTP e-mail test

This is a test e-mail message.
Hemlo vro!!! XD
"""

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
server.ehlo() 
server.login(os.getenv('EMAIL'), os.getenv('PASSWORD')) 

server.sendmail(sender,recievers,message)
print('successfully sent an email')
