import os
import smtplib
import ssl

port = 465

smtp_server = 'smtp.gmail.com'
sender_email = 'pulkitmahajan0402@gmail.com'
reciever_email = ['yashjaincp@gmail.com','temporary2021000@gmail.com']

password = input("Type in your password: ")
name = input()

message = """\
Subject: Hi There!!

www.gmail.com
This email was generated using a python script!
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message)
    print("Email sent")