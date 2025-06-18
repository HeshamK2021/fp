import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Title and Description
st.title("TradeMind - Crypto Advisor Prototype")
st.markdown("This is a feature prototype of TradeMind. It demonstrates a simple moving average strategy and mock advice system using dummy data.")

# Simulate dummy price data
np.random.seed(42)
dates = pd.date_range(end=datetime.datetime.today(), periods=100)
prices = np.cumsum(np.random.randn(100)) + 100
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)

# Calculate moving averages
df["MA_5"] = df["Price"].rolling(window=5).mean()
df["MA_20"] = df["Price"].rolling(window=20).mean()

# Generate signal
df["Signal"] = 0
df["Signal"][df["MA_5"] > df["MA_20"]] = 1
df["Signal"][df["MA_5"] < df["MA_20"]] = -1
latest_signal = df["Signal"].iloc[-1]

# Display chart
st.line_chart(df[["Price", "MA_5", "MA_20"]])

# Display recommendation
if latest_signal == 1:
    st.success("📈 Recommendation: BUY - Short-term trend shows bullish movement.")
elif latest_signal == -1:
    st.error("📉 Recommendation: SELL - Market is showing signs of decline.")
else:
    st.info("🤔 Recommendation: HOLD - No clear trend detected.")

# Explanation Section
with st.expander("Why this recommendation?"):
    st.write("""
        TradeMind uses a simple moving average crossover strategy in this prototype.
        When the 5-day MA crosses above the 20-day MA, it suggests an upward trend (BUY).
        When the 5-day MA crosses below the 20-day MA, it signals a potential downturn (SELL).
    """)
