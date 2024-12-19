import pandas as pd
import os 

#Folder path where the data files are located a
data_folder = "../data"

#load and preprocess financial news data
def preprocess_news_data():
    # Load the Financial news dataset
    news_data = pd.read_csv(os.path.join(data_folder, "Raw_analyst_ratings.csv"))
    
    # Drop rows with missing headlines or stock symbols
    news_data = news_data.dropna(subset=['headline', 'stock'])
    
    # Standardize the 'date' column to datetime format
    news_data['date'] = pd.to_datetime(news_data['date'].str.split(' ').str[0], errors='coerce', utc=True)
    
    # Drop rows with invalid dates
    news_data = news_data.dropna(subset=['date'])

    return news_data

# Load and preprocess stock data
def preprocess_stock_data():
        stock_files = [
        "AAPL_historical_data.csv", "AMZN_historical_data.csv", "GOOG_historical_data.csv",
        "META_historical_data.csv", "MSFT_historical_data.csv", "NVDA_historical_data.csv", "TSLA_historical_data.csv"
    ]
        stock_data = {}

        for file in stock_files:
              # Load each stock file
              stock_df = pd.read_csv(os.path.join(data_folder, file))

              # Convert all column names to lowercase
              stock_df.columns = stock_df.columns.str.lower()
              
              # Standardize the 'date' column to datetime format
              stock_df['date'] = pd.to_datetime(stock_df['date'].str.split(' ').str[0], errors='coerce', utc=True)

              # Drop rows with invalid dates
              stock_df = stock_df.dropna(subset=['date'])

              # Add the data to the dictionary with the ticker as the key
              ticker = file.split('_')[0]  # Use the stock ticker (e.g., 'AAPL') as the key
              stock_data[ticker] = stock_df

        return stock_data
