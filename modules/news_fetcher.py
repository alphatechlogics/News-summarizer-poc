import requests
import streamlit as st
from modules.config import API_KEY

def fetch_news(ticker, page_size=5):
    """Fetches news related to the specified ticker symbol."""
    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&pageSize={page_size}&sortBy=publishedAt&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("articles", [])
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching news for {ticker}: {e}")
        return []