import gspread
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def _get_sheet_name():
    if "SHEET_NAME" in st.secrets:
        return st.secrets["SHEET_NAME"]
    return os.getenv("SHEET_NAME")


def _get_client():
    if "gcp_service_account" in st.secrets:
        return gspread.service_account_from_dict(dict(st.secrets["gcp_service_account"]))
    return gspread.service_account(filename=os.getenv("GOOGLE_CREDENTIALS_PATH"))


def get_sheet():
    gc = _get_client()
    sh = gc.open(_get_sheet_name())
    return sh.sheet1


def get_new_leads():
    sheet = get_sheet()
    rows = sheet.get_all_records()
    pending = []
    for i, row in enumerate(rows):
        if row.get("Status") == "Pending" or row.get("Status") == "":
            pending.append((i+2, row))
    return pending
