import streamlit as st
from constants import STATE_VACANCY_SERIES, FRED_BASE_URL
from utils import fetch_data
import os


def _safe_secret(key):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        return None
    return None


def enrich_vacancy_rate(lead):
    state = lead.get("State", "").upper().strip()
    series_id = STATE_VACANCY_SERIES.get(state)

    if not series_id:
        lead["Rental Vacancy Rate"] = None
        return 

    params = {
        "series_id": series_id,
        "api_key": _safe_secret("FRED_API_KEY") or os.getenv("FRED_API_KEY"),
        "file_type": "json",
        "sort_order": "desc",
        "limit": 1
    }

    fred_data = fetch_data(FRED_BASE_URL, params)
    print(f"fred data: {fred_data}")
    observations = fred_data.get("observations", [])
    if not observations:
        lead["Rental Vacancy Rate"] = None
        return
    
    print(observations)
    value = observations[0]["value"]
    if value != "":
        lead["Rental Vacancy Rate"] = float(value)
    else:
        lead["Rental Vacancy Rate"] = None
        return

