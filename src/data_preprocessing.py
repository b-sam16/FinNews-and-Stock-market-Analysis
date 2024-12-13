import pandas as pd

# Function to load and clean stock data
def load_stock_data(file_path):
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)
    
    # Check for missing values and handle them (optional, e.g., drop rows with missing values)
    data.dropna(inplace=True)
    
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    
    return data

# Load stock data for AAPL, AMZN, GOOG, etc.
aapl_data = load_stock_data('./data/AAPL_historical_data.csv')
amzn_data = load_stock_data('./data/AMZN_historical_data.csv')
goog_data = load_stock_data('./data/GOOG_historical_data.csv')
meta_data = load_stock_data('./data/META_historical_data.csv')
msft_data = load_stock_data('./data/MSFT_historical_data.csv')
nvda_data = load_stock_data('./data/NVDA_historical_data.csv')
tsla_data = load_stock_data('./data/TSLA_historical_data.csv')

# Display the first few rows of AAPL data
print(aapl_data.head())
