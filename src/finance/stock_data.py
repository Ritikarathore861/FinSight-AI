# import yfinance as yf

# apple = yf.Ticker("AAPL")

# data = apple.history(period="5d")

# print(data)
# print(type(data))

# =========================
# DAY 3
# Return Calculation
# =========================

def calculate_return(open_price , close_price):
    return_percentage = (close_price-open_price)/open_price*100
    return return_percentage
result = calculate_return(200,220)
print("expected Return:", result,"%")
   