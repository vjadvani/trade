import yfinance as yf
from datetime import datetime
import pandas as pd

def get_option_prices(ticker, strike_price, expiry_date, option_type):
    """
    Function to retrieve daily option prices for a given stock.

    Parameters:
    - ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    - strike_price: Strike price of the option
    - expiry_date: Expiry date of the option (format: 'YYYY-MM-DD')
    - option_type: Type of option ('call' or 'put')

    Returns:
    - List of tuples (date, price) where date is in 'YYYY-MM-DD' format.
    """
    # Fetch the option chain for the specified expiry date
    stock = yf.Ticker(ticker)
    option_chain = stock.option_chain(expiry_date)

    # Select either the call or put option data
    if option_type == 'call':
        option_data = option_chain.calls
    elif option_type == 'put':
        option_data = option_chain.puts
    else:
        raise ValueError("Invalid option type. Please use 'call' or 'put'.")

    # Filter by strike price
    option_data_filtered = option_data[option_data['strike'] == strike_price]

    # Extract date and price information
    dates = option_data_filtered['lastTradeDate']
    prices = option_data_filtered['lastPrice']
    
    # Format dates and prices into list of tuples

    return dates, prices

def get_stock_data(ticker, start_date, end_date):
    """
    Function to retrieve daily stock data for a given ticker symbol.

    Parameters:
    - ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    - start_date: Start date for fetching data (format: 'YYYY-MM-DD')
    - end_date: End date for fetching data (format: 'YYYY-MM-DD')

    Returns:
    - Pandas DataFrame containing daily stock data with columns: Date, Open, High, Low, Close, Volume.
    """
    # Fetch the stock data using yfinance
    stock = yf.download(ticker, start=start_date, end=end_date)

    # Extracting required columns (Open, High, Low, Close, Volume)
    stock_data = stock[['Open', 'High', 'Low', 'Close', 'Volume']]

    return stock_data

# Example usage:
ticker = 'AAPL'
strike_price = 220.0
expiry_date = '2024-07-19'
option_type = 'call'
start_date = '2024-04-01'
end_date = '2024-06-30'

optiondates, option_prices = get_option_prices(ticker, strike_price, expiry_date, option_type)
df = pd.DataFrame({'date': optiondates})
df1 = pd.DataFrame({'price': option_prices})
merged_df = pd.merge(df, df1, left_index=True, right_index=True)
merged_df = merged_df.reset_index(drop=True)
print(merged_df)

stock_data = get_stock_data(ticker, start_date, end_date)
print(stock_data.head())
