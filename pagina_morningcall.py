import streamlit as st
import yfinance as yf

st.title("☕ Morning Call")

# Quick Market Check
cols = st.columns(4)
indices = {"^GSPC": "S&P 500", "^IXIC": "Nasdaq", "GC=F": "Goud", "BTC-USD": "Bitcoin"}

for i, (sym, name) in enumerate(indices.items()):
    tick = yf.Ticker(sym)
    hist = tick.history(period="2d")
    if len(hist) >= 2:
        price = hist['Close'].iloc[-1]
        change = ((price - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
        cols[i].metric(name, f"{price:,.2f}", f"{change:.2f}%")

st.markdown("---")
st.subheader("📰 Market News Feed")

# Iframe voor jouw nieuwsbron
news_url = "https://markets.financialcontent.com/stocks/markets/news/"
st.components.v1.iframe(news_url, height=1000, scrolling=True)
