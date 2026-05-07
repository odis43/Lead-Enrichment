import json
import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def _safe_secret(key):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        return None
    return None

client = genai.Client(api_key=_safe_secret("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY"))

def score_and_reasoning(lead):
    prompt = f"""
    You are a sales intelligence assistant for EliseAI, an AI platform
    that automates leasing conversations for property managers.

    EliseAI's ideal customer is a property management company operating
    in a high-volume rental market — high renter percentage, low vacancy
    rate, large market size, and a professionally managed property.

    Score this lead from 0-100 based on their fit for EliseAI.
    Be precise and critical — not every lead should score above 70.

    Lead:
    - Name: {lead.get('Name')}
    - Company: {lead.get('Company')}
    - City/State: {lead.get('City')}, {lead.get('State')}
    - Property: {lead.get('Property Address')}
    - Property name on Google: {lead.get('Property Name')}

    Market signals:
    - Renter %: {lead.get('Renter Percentage')}%
    - Rental vacancy rate: {lead.get('Rental Vacancy Rate')}%
    - Total housing units: {lead.get('Housing Units')}
    - Property Google review count: {lead.get('Property Review Count')}
    - Property Google rating: {lead.get('Property Rating')}

    Return a JSON object with exactly these keys:
    - score: integer 0-100
    - priority: one of "hot", "warm", "cold"
    - reasoning: 2-3 sentences explaining the score using specific signals
    - talking_points: list of exactly 3 strings, each a specific talking
      point for the SDR referencing actual data from the signals
    - email_subject: a short subject line for the first-touch email.
    - draft_email: a personalized first-touch email body under 100 words,
      written as a single continuous paragraph. Use the market data
      naturally and do not sound like a template.
      IMPORTANT: the draft_email value must contain NO newline characters,
      no "\\n", no carriage returns, and no line breaks of any kind.
      Write it as one flowing paragraph so the SDR can paste it directly
      into any field. Do not include the subject line inside draft_email.

    Return only valid JSON. No preamble, no markdown backticks.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            max_output_tokens=1000,
        ),
    )

    result = json.loads(response.text)
    print(result)
    lead["Score"]          = result["score"]
    lead["Priority"]       = result["priority"]
    lead["Score Reasoning"]      = result["reasoning"]
    lead["Draft Email"]    = result["draft_email"]
