from utils import fetch_data
from constants import STATE_FIPS, CENSUS_BASE_URL, CENSUS_VARIABLES, CENSUS_TOTAL_OCCUPIED_UNITS, CENSUS_RENTER_OCCUPIED_UNITS, CENSUS_TOTAL_HOUSING_UNITS
import streamlit as st
def enrich_census(lead):
    state = lead.get("State").upper().strip()
    state_to_fips = STATE_FIPS.get(state)
    if not state_to_fips:
        return None
    
    params = {
        "get": CENSUS_VARIABLES,
        "for": f"state:{state_to_fips}",
        }
    data = fetch_data(CENSUS_BASE_URL, params)
    if not data or len(data) == 0:
        return None
    
    headers = data[0]
    values = data[1]

    row = dict(zip(headers, values))
    total_occupied = int(row.get(CENSUS_TOTAL_OCCUPIED_UNITS))
    renter_occupied = int(row.get(CENSUS_RENTER_OCCUPIED_UNITS))
    if total_occupied == 0:
        return None
    renter_percentage = renter_occupied / total_occupied * 100
    lead["Housing Units"] = int(row.get(CENSUS_TOTAL_HOUSING_UNITS))
    lead["Renter Percentage"] = renter_percentage