import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title("TradeMind Bot Prototype")
st.markdown("This is a feature prototype of TradeMind. It demonstrates a simple moving average strategy and mock advice system using dummy data.")

# Generating random price data
np.random.seed(42)
dates = pd.date_range(end=datetime.datetime.today(), periods=100)
prices = np.cumsum(np.random.randn(100)) + 100
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)

# Calculating the moving averages  for MA5 & MA20
df["MA_5"] = df["Price"].rolling(window=5).mean()
df["MA_20"] = df["Price"].rolling(window=20).mean()

# Generating signal
df["Signal"] = 0
df["Signal"][df["MA_5"] > df["MA_20"]] = 1
df["Signal"][df["MA_5"] < df["MA_20"]] = -1
latest_signal = df["Signal"].iloc[-1]

# Displaying the prices chart
st.line_chart(df[["Price", "MA_5", "MA_20"]])

# Displaying the signal recommendation
if latest_signal == 1:
    st.success("📈 Recommendation: BUY! Market Trend is Bullish shows bullish movement.")
elif latest_signal == -1:
    st.error("📉 Recommendation: SELL! Market Trend is Berish")
else:
    st.info("🤔 Recommendation: HOLD! - Unable to detect a clear Movement.")

# Explanation Section
with st.expander("Why this recommendation?"):
    st.write("""
        TradeMind uses a simple moving average crossover strategy in this prototype.
        When the 5-day MA crosses above the 20-day MA, it suggests an upward trend (BUY).
        When the 5-day MA crosses below the 20-day MA, it signals a potential downturn (SELL).
    """)
