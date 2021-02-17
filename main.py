import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import os
import pandas as pd
import numpy as np
from email_script import generate_email
from dotenv import load_dotenv


load_dotenv()

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json' , scope)
client = gspread.authorize(creds)


sheet = client.open("sample_sheet").sheet1
data = sheet.get_all_records()



# psswd = input('Enter your password: ')

for (index, entry) in enumerate(data):
    try:
        print("\nEmail Generation Initiated")
        generate_email(entry_dict = entry)
    except Exception as e:
        # print(e.message)
        print("Error occured, Email could not be sent to {name}, order no.: {order_no}".format(name = entry['Name'].capitalize(),order_no = entry['Order_No']))
        sheet.update_cell(row = index+2 , col = 8, value=False)

    else:
        print("Email successfully sent to {name}, {order_no}".format(name = entry['Name'],order_no = entry['Order_No']))
        sheet.update_cell(row = index+2 , col = 8, value=True)
    finally:
        if index == len(data)-1: print('Finished with all entries\n')
        else : print("Moving to next entry \n")
        


