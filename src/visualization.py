import pandas as pd
import matplotlib.pyplot as plt
from technical_Indicators import calculate_technical_indicators

def plot_stock_prices(stock_data, ticker):
    """
    Plot the stock prices over time for a specific ticker.

    Parameters:
    - stock_data: Dictionary containing stock DataFrames (key=ticker, value=DataFrame).
    - ticker: String, the ticker symbol to visualize.
    """
    df = stock_data[ticker]
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['close'], label='Close Price', color='blue')
    plt.title(f'{ticker} Stock Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()

def plot_stock_with_indicators(stock_data, ticker):
    """
    Plot the stock price along with Moving Average, RSI, and MACD.
    
    Parameters:
    - stock_data: Dictionary containing stock DataFrames.
    - ticker: The stock ticker symbol.
    """
    df = stock_data[ticker]
    df = calculate_technical_indicators(df)  # Apply technical indicators to the data
        
    # Plotting Stock Price and Moving Average
    fig, ax = plt.subplots(3, 1, figsize=(12, 12))

    # Stock Price with Moving Average
    ax[0].plot(df['date'], df['close'], label='Close Price', color='blue')
    ax[0].plot(df['date'], df['MA'], label='20-day MA', color='orange')
    ax[0].set_title(f'{ticker} Stock Prices with 20-day Moving Average')
    ax[0].set_ylabel('Price')
    ax[0].legend()

    # RSI Plot
    ax[1].plot(df['date'], df['RSI'], label='RSI', color='green')
    ax[1].axhline(70, linestyle='--', color='red', label='Overbought (70)')
    ax[1].axhline(30, linestyle='--', color='blue', label='Oversold (30)')
    ax[1].set_title(f'{ticker} Relative Strength Index (RSI)')
    ax[1].set_ylabel('RSI')
    ax[1].legend()

    # MACD Plot
    ax[2].plot(df['date'], df['MACD'], label='MACD', color='purple')
    ax[2].plot(df['date'], df['MACD_signal'], label='Signal Line', color='orange')
    ax[2].set_title(f'{ticker} MACD and Signal Line')
    ax[2].set_ylabel('Value')
    ax[2].legend()

    plt.tight_layout()
    plt.show()
