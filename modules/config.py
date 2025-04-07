from dotenv import load_dotenv
import os

load_dotenv()

# Load environment variables from .env file
API_KEY = os.getenv("API_KEY")

SECTOR_KEYWORDS = {
    "Technology": ["tech", "software", "hardware", "ai", "artificial intelligence", "cloud", "computing", 
                  "semiconductor", "chip", "digital", "internet", "app", "mobile", "cybersecurity"],
    "Healthcare": ["health", "medical", "pharma", "biotech", "drug", "vaccine", "therapeutic", "patient", 
                  "clinical", "hospital", "medicine", "disease", "treatment", "diagnostic"],
    "Financial": ["bank", "finance", "financial", "insurance", "invest", "capital", "credit", "loan", 
                 "mortgage", "wealth", "payment", "fintech", "trading", "stock market"],
    "Energy": ["energy", "oil", "gas", "power", "renewable", "solar", "wind", "coal", "electricity", 
              "fuel", "petroleum", "drilling", "battery", "carbon", "climate"],
    "Consumer Discretionary": ["retail", "consumer", "ecommerce", "luxury", "entertainment", "travel", 
                             "automotive", "apparel", "restaurant", "hotel", "leisure"],
    "Consumer Staples": ["food", "beverage", "household", "grocery", "supermarket", "personal care", 
                        "consumer staples", "tobacco", "packaged goods"],
    "Telecommunications": ["telecom", "communication", "wireless", "broadband", "5g", "network", 
                          "satellite", "mobile network", "internet service"],
    "Industrial": ["manufacturing", "industrial", "aerospace", "defense", "construction", "machinery", 
                  "transportation", "logistics", "infrastructure"],
    "Materials": ["materials", "chemical", "metal", "mining", "steel", "paper", "packaging"],
    "Real Estate": ["real estate", "property", "reit", "commercial property", "residential", "housing"]
}

COMMON_TICKERS = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "GOOGL": "Google",
    "GOOG": "Google",
    "AMZN": "Amazon",
    "META": "Meta",
    "TSLA": "Tesla",
    "NVDA": "NVIDIA",
    "NFLX": "Netflix",
    "JNJ": "Johnson & Johnson",
    "JPM": "JPMorgan Chase",
    "XOM": "Exxon Mobil",
    "WMT": "Walmart",
    "V": "Visa",
    "PG": "Procter & Gamble",
    "DIS": "Disney",
    "HD": "Home Depot",
    "BAC": "Bank of America",
    "KO": "Coca-Cola",
    "VZ": "Verizon"
}