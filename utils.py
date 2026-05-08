import requests
import streamlit as st
def fetch_data(url, params):
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch {url} due error: {e}")
        return None





