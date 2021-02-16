import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from templates.template import giveTemplate
from dotenv import load_dotenv
load_dotenv()

# port = 465

# smtp_server = 'smtp.gmail.com'
# sender_email = os.getenv('SENDER_EMAIL')

# password = input("Type in your password: ")
# # name = input()

# message = """\
# Subject: Hi There {name}!!

# www.gmail.com
# This email was generated using a python script!
# """

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, reciever_email, message)
#     print("Email sent")



def generate_email(entry_dict):
    """entry_dict: a tuple representing a row of the sheet"""
    #parsing arguments
    
    order_no = entry_dict['Order_No']
    name = entry_dict['Name']

    email_id = entry_dict['Email_ID']
    tracking_details = entry_dict['Tracking_Details']
    ref_no_refund = entry_dict['Ref_no_Refund']
    amount = entry_dict['Amount']
    template = entry_dict['Template']


    sender_email = os.getenv('SENDER_EMAIL')
    api_key = os.getenv("SENDGRID_API_KEY")

    (text, html) = giveTemplate(template)
    
    message = Mail(from_email = sender_email
              ,to_emails = email_id
              ,subject = template
              ,plain_text_content = text.format(name = name, tracking_details = tracking_details, order_id = order_no, ref_no_refund = ref_no_refund, amount = amount )
              ,html_content = html.format(name = name, tracking_details = tracking_details, order_id = order_no, ref_no_refund = ref_no_refund, amount = amount )
              )
    
    sg = SendGridAPIClient(api_key)
    sg.send(message)
    

    


# print(os.getenv('SENDER_EMAIL'))
