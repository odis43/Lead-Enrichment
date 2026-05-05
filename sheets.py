import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
sheets_name = os.getenv("SHEET_NAME")
credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")

def get_sheet():
    gc = gspread.service_account(filename=credentials_path)
    sh = gc.open(sheets_name)
    return sh.sheet1

def get_new_leads():
    sheet = get_sheet()
    rows = sheet.get_all_records()
    pending = []
    for i, row in enumerate(rows):
        if row.get("Status") == "Pending" or row.get("Status") == "":
            pending.append((i+2, row))
    return pending
    
    
    
