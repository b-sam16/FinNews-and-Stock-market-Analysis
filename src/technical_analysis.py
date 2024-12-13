import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pandas as pd
import talib
from data_preprocessing import load_stock_data  # After adjusting sys.path

# Function to apply TA-Lib indicators to stock data
def apply_technical_indicators(data):
    # Calculate Simple Moving Averages (SMA)
    data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
    data['SMA_200'] = talib.SMA(data['Close'], timeperiod=200)
    
    # Calculate Relative Strength Index (RSI)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    
    # Calculate MACD and Signal Line
    data['MACD'], data['MACD_signal'], _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    return data

# Load stock data for AAPL
aapl_data = load_stock_data('./data/AAPL_historical_data.csv')  # This loads the stock data

# Apply the technical indicators to the AAPL stock data
aapl_data = apply_technical_indicators(aapl_data)

# Display the first few rows of the updated AAPL data with technical indicators
print(aapl_data[['Date', 'SMA_50', 'SMA_200', 'RSI', 'MACD']].head())
