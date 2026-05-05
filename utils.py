import requests
import streamlit as st
def fetch_data(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.write(f"Could not fetch {url} due error: {e}")
        return None





