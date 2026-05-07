import gspread, gspread.utils
import os
from dotenv import load_dotenv
import streamlit as st
from constants import WRITE_FIELDS

load_dotenv()


def _safe_secret(key):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        return None
    return None


def _get_sheet_name():
    return _safe_secret("SHEET_NAME") or os.getenv("SHEET_NAME")


def _get_client():
    gcp = _safe_secret("gcp_service_account")
    if gcp is not None:
        return gspread.service_account_from_dict(dict(gcp))
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
        if row.get("Status") == "Pending" or row.get("Status") == "" or row.get("Status") == None:
            pending.append((i+2, row))
    return pending

def write_back(updated_leads):
    ws = get_sheet()
    headers = ws.row_values(1)

    missing = [f for f in WRITE_FIELDS if f not in headers]
    if missing:
        headers = headers + missing
        ws.update(range_name="A1", values=[headers])

    col_for = {h: i + 1 for i, h in enumerate(headers)}

    requests = []
    for row, lead in updated_leads:
        for field in WRITE_FIELDS:
            if field in lead:                       
                a1 = gspread.utils.rowcol_to_a1(row, col_for[field])
                requests.append({"range": a1, "values": [[lead[field]]]})
    if requests:
        ws.batch_update(requests)