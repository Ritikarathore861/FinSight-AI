import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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


print("\n----- Stock Comparison -----")

stock1 = input("Enter First Stock: ").upper()
stock2 = input("Enter Second Stock: ").upper()

data1 = yf.Ticker(stock1).history(period="5d")
data2 = yf.Ticker(stock2).history(period="5d")

close1 = data1["Close"].dropna().iloc[-1]
close2 = data2["Close"].dropna().iloc[-1]

print(stock1, "Latest Close:", round(close1, 2))
print(stock2, "Latest Close:", round(close2, 2))


open1 = data1["Open"].dropna().iloc[-1]
open2 = data2["Open"].dropna().iloc[-1]

return1 = ((close1 - open1) / open1) * 100
return2 = ((close2 - open2) / open2) * 100

return1 = round(return1, 2)
return2 = round(return2, 2)

print(stock1, "Return:", return1, "%")
print(stock2, "Return:", return2, "%")

if return1 > return2:
    print("🏆 Better Performing Stock:", stock1)

elif return2 > return1:
    print("🏆 Better Performing Stock:", stock2)

else:
    print("🤝 Both Stocks Performed Equally")   

report_data = {
    "Stock": [stock1, stock2],
    "Return": [return1, return2]
}

report_df = pd.DataFrame(report_data)

report_df.to_csv("stock_report.csv", index=False)

print(" Report saved as stock_report.csv")


# Stock Price Chart
# Visualizing Closing Prices

plt.plot(data.index, data["Close"])

plt.title(f"{ticker_symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Close Price")

plt.show()