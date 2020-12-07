# pip install gspread
# pip install --upgrade oauth2client
# https://docs.google.com/spreadsheets/d/1IbrA4S_BhTCtIHZpxoDA6UaYh_D4nIpQwT6iuZNaGqA/edit#gid=0


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'chatbot-290215-0a20b22f1b6a.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1IbrA4S_BhTCtIHZpxoDA6UaYh_D4nIpQwT6iuZNaGqA/edit#gid=0'

doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet('시트1')
print(worksheet.row_values(1))

