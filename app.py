import streamlit as st
from pipeline import run_pipline
import time 

st.write("Secrets keys:", list(st.secrets.keys()))
st.stop()

st.title("LET (lead enrichment tool)")
if st.button("Process leads"):
    with st.spinner(text="Processing..."):
        run_pipline()

    st.success(f"Processed: {0} new leads.  See sheets!")


