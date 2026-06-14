import yfinance as yf

# apple = yf.Ticker("AAPL")
ticker_symbol = input("Enter Stock Ticker: ")
investment = float(input("Enter Investment Amount: ₹"))
stock = yf.Ticker(ticker_symbol)
# print("Investment Amount:", investment)

data = stock.history(period="5d")
print("\n========== FinSight AI ==========\n")
print(data)

# print(type(data))

# =========================
# DAY 3
# Return Calculation
# =========================


latest_close = data["Close"].dropna().iloc[-1]
latest_open = data["Open"].dropna().iloc[-1]

# print("Latest Close Price:", latest_close)
# print("Latest Open Price:", latest_open)


def calculate_return(open_price , close_price):
    return_percentage = (close_price-open_price)/open_price*100
    return return_percentage
# result = calculate_return(200,220)
result = calculate_return(latest_open, latest_close)
# print("expected Return:", result,"%")

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


print("----- Stock Analysis -----")

print("Stock:", ticker_symbol)
print("Rounded Open Price:", rounded_open)
print("Rounded Close Price:", rounded_close)
print("Expected Return:", rounded_return, "%")

if rounded_return > 0:
    print("📈 Stock went up")
else:
    print("📉 Stock went down")




highest_close = data["Close"].max()
lowest_close = data["Close"].min()


highest_close_rounded = round(highest_close, 2)
lowest_close_rounded = round(lowest_close, 2)

print("Highest Close Price:", highest_close_rounded)
print("Lowest Close Price:", lowest_close_rounded)


average_close = data["Close"].mean()
average_close_rounded = round(average_close, 2)
print("Average Close Price:", average_close_rounded)


profit = investment * rounded_return / 100
profit_rounded = round(profit, 2)
# print("Profit/Loss: ₹", profit_rounded)

print("\n----- Investment Summary -----")
print("Investment Amount: ₹", investment)
print("Profit/Loss: ₹", profit_rounded)

final_value = investment + profit_rounded
final_value_rounded = round(final_value, 2)
print("Final Value: ₹", final_value_rounded)


if rounded_return > 5:
    print("🚀 Performance: Excellent")

elif rounded_return > 0:
    print("📈 Performance: Good")

elif rounded_return == 0:
    print("➖ Performance: Neutral")

else:
    print("📉 Performance: Poor")

if rounded_return > 5:
    print("🚀 Suggestion: BUY")

elif rounded_return > 0:
    print("👍 Suggestion: HOLD")

else:
    print("⚠️ Suggestion: SELL")