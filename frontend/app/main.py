import streamlit as st
import requests

base_url = "http://127.0.0.1:8000"

with st.container(border=True):
    text_to_summarized = st.text_area("Summarized text", placeholder="Enter a text to summarize")
    if st.button("submit"):
        api_url = f"{base_url}/process-text"
        params = {"text": text_to_summarized}
        response = requests.post(api_url, params=params)
        try:
            if response.status_code == 200:
                st.text_area("Summarized text", value=response.text)
        except requests.exceptions.RequestException as e:
            st.warning("Something went wrong")
