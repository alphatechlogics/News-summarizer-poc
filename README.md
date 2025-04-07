# News Fetcher and Analyzer

This project is a Streamlit-based application that fetches and analyzes news articles related to a specific stock ticker. It provides sentiment analysis, summarization, and sector/ticker extraction for each article.

## Features
- Fetch news articles using the NewsAPI.
- Perform sentiment analysis using FinBERT.
- Summarize articles using BART.
- Extract related stock tickers and sectors from the article content.

## Project Structure
```
news_fetcher/
├── modules/
│   ├── config.py          # Configuration constants (API keys, keywords, etc.)
│   ├── news_fetcher.py    # Functions for fetching news articles
│   └── text_analysis.py   # Functions for text analysis (sentiment, summarization, etc.)
├── app.py    # Main Streamlit application
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd news_fetcher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Requirements
- Python 3.7+
- NewsAPI key (replace the placeholder in `config.py` with your key).

## Dependencies
See `requirements.txt` for the full list of dependencies.

## Usage
1. Enter a stock ticker symbol (e.g., AAPL, TSLA) in the sidebar.
2. Select the number of articles to fetch.
3. Click the "Fetch News" button to analyze the articles.

## License
This project is licensed under the MIT License.