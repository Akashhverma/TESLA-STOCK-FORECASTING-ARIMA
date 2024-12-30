import streamlit as st
import pandas as pd
import numpy as np
import pickle
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the pre-trained ARIMA model
with open('arima_model.pkl', 'rb') as f:
    arima_result = pickle.load(f)

# Function to fetch Tesla stock data (for demonstration purposes)
def fetch_data(ticker='TSLA'):
    data = yf.download(ticker, period="5y", interval="1d")
    return data

def forecast_arima(model, data, steps=1):
    # Last closing price
    last_close = data['Close'].iloc[-1]
    
    # Forecast the next steps (1 step for now)
    arima_forecast = model.forecast(steps=steps)
    
    # Access the first forecasted value from the Series
    forecast_value = last_close + arima_forecast.iloc[0]
    
    return forecast_value



# Streamlit app layout
st.title('Tesla Stock Price Forecasting using ARIMA')

# Fetch Tesla data
tsla_data = fetch_data()

# Display stock data
st.write("### Tesla Stock Data")
st.write(tsla_data.tail())

# Forecasting the next day's stock price
forecast_value = forecast_arima(arima_result, tsla_data)
forecast_value_scalar = forecast_value.item()
st.write(f"Next day forecasted close price: ${forecast_value:.2f}")

# Plot the actual and predicted prices
fig, ax = plt.subplots(figsize=(12, 6))
tsla_data['Close'].plot(ax=ax, label='Actual')
forecast_index = pd.date_range(start=tsla_data.index[-1], periods=2, freq='B')
forecast_series = pd.Series([tsla_data['Close'].iloc[-1], forecast_value], index=forecast_index)
forecast_series.plot(ax=ax, label='Forecast', linestyle='--')
plt.title('ARIMA Model - Tesla Stock Price Forecast')
plt.legend()
st.pyplot(fig)

