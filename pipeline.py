import streamlit as st
from enrichment.census import enrich_census
from sheets import get_new_leads
def run_pipline():
    leads = get_new_leads()
    st.write("Unfiltered leads:")
    st.write(leads)
    st.write("Filtered leads:")
    for _, lead in leads:
        enrich_census(lead)
    
    st.write(leads)


