import pandas as pd
import numpy as np
from data_preprocessing import preprocess_news_data, preprocess_stock_data
from sentiment_analysis import apply_sentiment_analysis
from visualization import plot_correlations



def compute_daily_returns(stock_data):
    """
    Calculate daily returns for each stock in the stock_data dictionary.
    """
    for stock_ticker, stock_df in stock_data.items():
        stock_df['daily_return'] = stock_df['close'].pct_change()
        stock_data[stock_ticker] = stock_df
    return stock_data

def calculate_correlation(news_data, stock_data):
    """
    Calculate the correlation between sentiment scores in news_data 
    and daily stock returns in stock_data.
    """
    correlations = {}

    # Ensure column consistency
    news_data.columns = news_data.columns.str.strip()

    for stock_ticker, stock_df in stock_data.items():
        stock_df.columns = stock_df.columns.str.strip()

        # Ensure the 'date' columns are in datetime format
        news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')
        stock_df['date'] = pd.to_datetime(stock_df['date'], errors='coerce')

        # Drop rows where 'date' is invalid
        news_data = news_data.dropna(subset=['date'])
        stock_df = stock_df.dropna(subset=['date'])

        # Merge news_data and stock_df on 'date'
        merged_data = pd.merge(news_data, stock_df[['date', 'daily_return']], on='date', how='inner')

        # Debugging: Check if merged_data has sufficient rows for correlation calculation
        print(f"Merged data for {stock_ticker} has {len(merged_data)} rows")

        if len(merged_data) > 1:  # Correlation requires at least two data points
            # Ensure there is data for both sentiment and daily returns
            if 'sentiment_numeric' in merged_data.columns and 'daily_return' in merged_data.columns:
                # Check for NaN values in sentiment or daily returns
                print(f"Missing values in sentiment or daily return for {stock_ticker}:",
                      merged_data[['sentiment_numeric', 'daily_return']].isna().sum())

                # Drop rows with NaN values
                merged_data = merged_data.dropna(subset=['sentiment_numeric', 'daily_return'])

                # Debugging: Check for constant data or lack of variation
                print(f"Sentiment data for {stock_ticker}: {merged_data['sentiment_numeric'].describe()}")
                print(f"Stock returns data for {stock_ticker}: {merged_data['daily_return'].describe()}")

                # Calculate correlation
                correlation = merged_data['sentiment_numeric'].corr(merged_data['daily_return'])

                if np.isnan(correlation):
                    print(f"Correlation for {stock_ticker} is NaN due to lack of data variation or overlap.")
                else:
                    correlations[stock_ticker] = correlation
            else:
                print(f"Missing sentiment or daily return data for {stock_ticker}. Skipping correlation calculation.")
        else:
            print(f"Not enough overlapping data to calculate correlation for {stock_ticker}. Skipping.")

    return correlations
