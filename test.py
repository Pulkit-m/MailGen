import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import os 
import pandas as pd

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json' , scope)
client = gspread.authorize(creds)
email_id = os.getenv('EMAIL')
pwd = os.getenv('PASSWORD')


sheet = client.open("sample_sheet").sheet1
data = sheet.get_all_records()

df = pd.DataFrame(data)
print(df.head(9),'\n','\n')

print(df[df['email sent or not']==0]['Email Id'].unique())

pprint(df)