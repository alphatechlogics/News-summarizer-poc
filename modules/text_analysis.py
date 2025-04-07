import re
from transformers import pipeline
from modules.config import SECTOR_KEYWORDS, COMMON_TICKERS
import streamlit as st

@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="YarbHelp/Stock-News-Sentiment-Analysis")

@st.cache_resource
def load_summarizer_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

sentiment_model = load_sentiment_model()
summarizer_model = load_summarizer_model()

def clean_text(text):
    """Clean and preprocess the text for better model performance."""
    if not text:
        return ""
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = re.sub(r'[^\w\s$.]', ' ', cleaned_text)
    return cleaned_text.strip()

def extract_tickers_from_text(text):
    """Extract stock tickers using regex patterns and company name mentions."""
    ticker_pattern = r'\$([A-Z]{1,5})\b'
    direct_tickers = re.findall(ticker_pattern, text.upper())
    possible_tickers = re.findall(r'\b([A-Z]{2,5})\b', text)
    common_words = {"THE", "AND", "FOR", "NEW", "CEO", "CFO", "CTO", "COO", "IPO", "NYSE", "NASDAQ"}
    filtered_tickers = [t for t in (direct_tickers + possible_tickers) if t not in common_words]
    found_tickers = set(filtered_tickers)
    for ticker, company in COMMON_TICKERS.items():
        if company.lower() in text.lower() and ticker not in found_tickers:
            found_tickers.add(ticker)
    return list(found_tickers)

def extract_sectors_from_text(text):
    """Extract potential sectors from text using keyword matching."""
    text_lower = text.lower()
    sectors = {}
    for sector, keywords in SECTOR_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            score += text_lower.count(keyword)
        if score > 0:
            sectors[sector] = score
    if not sectors:
        return []
    sorted_sectors = sorted(sectors.items(), key=lambda x: x[1], reverse=True)
    return [sector for sector, score in sorted_sectors[:3]]

def analyze_article(article):
    """Analyze a news article for sentiment, summary, tickers, and sectors."""
    title = article.get("title", "")
    content = article.get("content", "")
    description = article.get("description", "")
    full_text = f"{title} {description} {content}"
    cleaned_text = clean_text(full_text)
    try:
        sentiment = sentiment_model(cleaned_text[:512])[0]["label"]
    except Exception as e:
        sentiment = "Unknown"
        st.error(f"Error in sentiment analysis: {e}")
    try:
        if len(cleaned_text) > 100:
            summary = summarizer_model(cleaned_text[:1024], max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
        else:
            summary = description or title
    except Exception as e:
        summary = description or title
        st.error(f"Error in summarization: {e}")
    tickers = extract_tickers_from_text(full_text)
    sectors = extract_sectors_from_text(full_text)
    return {
        "title": title,
        "url": article.get("url", "N/A"),
        "tickers": tickers,
        "sectors": sectors,
        "sentiment": sentiment,
        "summary": summary
    }