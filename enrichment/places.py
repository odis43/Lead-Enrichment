import streamlit as st
from constants import PLACES_URL
from utils import fetch_data
import os
import requests


def _safe_secret(key):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        return None
    return None


def enrich_property(lead):
    state = lead.get("State", "").upper().strip()
    company = lead.get("Company", "")
    address = lead.get("Property Address", "")
    city = lead.get("City", "")
    state = lead.get("State", "")    
    query = f"{company} {address} {city} {state}"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": _safe_secret("PLACES_API_KEY") or os.getenv("PLACES_API_KEY"),
        "X-Goog-FieldMask": "places.displayName,places.rating,places.userRatingCount,places.formattedAddress,places.businessStatus,places.types"
    }

    body = {
        "textQuery": query,
        "maxResultCount": 1
    }

    try:
        response = requests.post(PLACES_URL, json=body, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()

        places = data.get("places", [])
        if not places:
            lead["Property Rating"] = None
            lead["Property Review Count"] = None
            lead["Property Name"] = None
            return
        print(f'Places: {places}')
        place = places[0]
        lead["Property Name"] = place.get("displayName", {}).get("text")
        lead["Property Rating"] = place.get("rating")
        lead["Property Review Count"] = place.get("userRatingCount")
        lead["Property Business Status"] = place.get("businessStatus")
    except Exception as e:
        st.write(f"Could not fetch property data: {e}")
        lead["Property Rating"] = None
        lead["Property Review Count"] = None
        lead["Property Name"] = None
        return 



