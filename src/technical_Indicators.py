import pandas as pd
import talib as ta

# Moving Average (MA)
def MA(df, period=14):
    df['MA'] = ta.SMA(df['Close'], timeperiod=period)
    return df

# Relative Strength Index (RSI)
def RSI(df, period=14):
    df['RSI'] = ta.RSI(df['Close'], timeperiod=period)
    return df

# Moving Average Convergence Divergence (MACD)
def MACD(df, fastperiod=12, slowperiod=26, signalperiod=9):
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(
        df['Close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod
    )
    return df

# Function to apply all technical indicators
def calculate_technical_indicators(df):
    df = MA(df)  # Add Moving Average
    df = RSI(df) # Add RSI
    df = MACD(df) # Add MACD
    return df

