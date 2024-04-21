import yfinance as yf
import streamlit as st
import datetime


# Create a Header
st.header("Stock Analysis App")

# Extract stock name from uer
stock = st.text_input("INPUT THE NAME OF THE STOCK", 'GOOG')
data = yf.Ticker(stock)

# Print Stock name which we are analysing
st.write("Currently Analysing: ", stock)
# get historical market data

# Break page into columns
col1, col2 = st.columns(2)
with col1:
    # Select Start Date
    start_date = st.date_input("Enter Start Date", datetime.date(2024, 1, 1))
with col2:
    # Select End Date
    end_date = st.date_input("Enter End Date", datetime.date(2024, 1, 31))

# Extract data from yfinance
hist = data.history(period="1d", start=start_date,
                    end=end_date)

# Print Dataframe
st.write(hist)

# Display Chart
st.subheader("Trend in closing prices:")
st.line_chart(hist['Close'])


st.subheader("Trend in Volume:")
st.bar_chart(hist['Volume'])
