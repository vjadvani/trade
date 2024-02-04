import yfinance as yf
msft = yf.Ticker("MSFT")
#abc = msft.info

#hist = msft.history(period="1mo")
#print(hist)

# show financials:
# - income statement
abc = msft.income_stmt
print(type(abc))
print(abc)
# msft.quarterly_income_stmt
# - balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet
# - cash flow statement
# msft.cashflow
# msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
holders = msft.major_holders
print(holders)
# msft.institutional_holders
# msft.mutualfund_holders
# msft.insider_transactions
# msft.insider_purchases
# msft.insider_roster_holders

# show recommendations
# msft.recommendations
# msft.recommendations_summary
# msft.upgrades_downgrades

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
# msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
# msft.isin

# show options expirations
# msft.options

# show news
# msft.news

# get option chain for specific expiration
#opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
