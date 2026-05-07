import streamlit as st
from pipeline import process_new_leads
st.title("ELET (EliseAI Lead Enrichment Tool)")

for _ in range(3):
    st.write("")

left, center, right = st.columns([1, 1, 1])
with center:
    clicked = st.button("Process new leads", use_container_width=True)

if clicked:
    with st.spinner(text="Processing..."):
        leads = process_new_leads()
    for row_index, lead in leads:
        if lead.get("Status") == "Error":
            st.warning(
                f"Lead row {row_index} ({lead.get('Name', '?')}): {lead.get('Error', 'Unknown error')}"
            )
    if len(leads) == 0:
        st.success("No new leads to enrich")
    else:
        st.write(leads)
        st.success(f"Processed: {len(leads)} new leads")
    st.page_link(page="https://docs.google.com/spreadsheets/d/17lwYqaJZ2Sxx7KRVMHOKmw3jQUE0H7pSLOJJEMzefWE/edit?gid=0#gid=0", label="Go to data")


