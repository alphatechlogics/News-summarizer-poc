import streamlit as st
st.set_page_config(page_title="News summarize and analyze", layout="wide")

from modules.news_fetcher import fetch_news
from modules.text_analysis import analyze_article


st.title("📊 News summarize and analyze")
st.sidebar.header("Configuration")

# User Inputs
ticker = st.sidebar.text_input("Enter Ticker Symbol", value="AAPL").upper()
num_articles = st.sidebar.slider("Number of Articles", min_value=1, max_value=10, value=5)

if st.sidebar.button("Fetch News"):
    st.write(f"📥 Fetching News for {ticker}...")
    articles = fetch_news(ticker, num_articles)

    if not articles:
        st.error("❌ No articles found.")
    else:
        st.success(f"📰 Found {len(articles)} articles related to {ticker}")

        # Create a matrix layout for displaying results
        for idx, article in enumerate(articles, start=1):
            result = analyze_article(article)

            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                st.subheader(f"Article {idx}: {result['title']}")
                st.write(f"**Summary:** {result['summary']}")
                st.write(f"[Read more]({result['url']})")

            with col3:
                st.metric(label="Sentiment", value=result['sentiment'].replace("LABEL_1", "Positive").replace("LABEL_2", "Negative").replace("LABEL_0", "Neutral"))
                st.metric(label="Tickers", value=', '.join(result['tickers']) if result['tickers'] else 'None')
                st.metric(label="Sectors", value=', '.join(result['sectors']) if result['sectors'] else 'None')