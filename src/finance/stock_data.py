import yfinance as yf

# apple = yf.Ticker("AAPL")
ticker_symbol = input("Enter Stock Ticker: ")
stock = yf.Ticker(ticker_symbol)

data = stock.history(period="5d")
 
print(data)

# print(type(data))

# =========================
# DAY 3
# Return Calculation
# =========================


latest_close = data["Close"].dropna().iloc[-1]
latest_open = data["Open"].dropna().iloc[-1]

print("Latest Close Price:", latest_close)
print("Latest Open Price:", latest_open)


def calculate_return(open_price , close_price):
    return_percentage = (close_price-open_price)/open_price*100
    return return_percentage
# result = calculate_return(200,220)
result = calculate_return(latest_open, latest_close)
print("expected Return:", result,"%")

# =========================
# DAY 4
# Close Price Column
# =========================

# print(data["Close"])
# print(data["Close"].dropna())

# latest_close = data["Close"].dropna().iloc[-1]

# print("Latest Close Price:", latest_close)


# # day5
# latest_open = data["Open"].dropna().iloc[-1]
# print("Latest Open Price:", latest_open)
rounded_open = round(latest_open, 2)
rounded_close = round(latest_close, 2)
rounded_return = round(result, 2)

print("Rounded Open Price:", rounded_open)
print("Rounded Close Price:", rounded_close)
print("Expected Return:", rounded_return, "%")
