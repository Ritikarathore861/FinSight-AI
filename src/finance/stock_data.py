import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# apple = yf.Ticker("AAPL")
ticker_symbol = input("Enter Stock Ticker: ")


investment = float(input("Enter Investment Amount: ₹"))
stock = yf.Ticker(ticker_symbol)
# print("Investment Amount:", investment)

data = stock.history(period="3mo")
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

if data1.empty or data2.empty:
    print("❌ Invalid stock ticker entered.")
    exit()

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

# plt.plot(data.index, data["Close"])

# plt.title(f"{ticker_symbol} Stock Price")
# plt.xlabel("Date")
# plt.ylabel("Close Price")

# plt.savefig("stock_chart.png")
# plt.show()


# Improve the Stock Chart
plt.figure(figsize=(10, 5))

plt.plot(
    data.index,
    data["Close"],
    marker="o",
    linestyle="-"
)

plt.title(f"{ticker_symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Close Price")

plt.grid(True)

plt.savefig("stock_chart.png")
print("📊 Chart saved as stock_chart.png")

plt.show()

# Day 23: Compare Two Stocks on the Same Graph
stock1_data = yf.Ticker(stock1).history(period="5d")
stock2_data = yf.Ticker(stock2).history(period="5d")


plt.figure(figsize=(10, 5))

plt.plot(
    stock1_data.index,
    stock1_data["Close"],
    marker="o",
    label=stock1
)

plt.plot(
    stock2_data.index,
    stock2_data["Close"],
    marker="o",
    label=stock2
)

plt.title(f"{stock1} vs {stock2}")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.legend()

plt.savefig("comparison_chart.png")
print("📊 Comparison chart saved as comparison_chart.png")

plt.show()

# Add Moving Average


data["MA5"] = data["Close"].rolling(window=5).mean()
plt.figure(figsize=(10, 5))

plt.plot(
    data.index,
    data["Close"],
    marker="o",
    label="Close Price"
)

plt.plot(
    data.index,
    data["MA5"],
    marker="o",
    label="5-Day Moving Average"
)

plt.title(f"{ticker_symbol} Stock Price with Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()

plt.savefig("moving_average_chart.png")
print("📊 Moving Average chart saved as moving_average_chart.png")

plt.show()


# Day 25: Add 10-Day Moving Average
data["MA10"] = data["Close"].rolling(window=10).mean()

plt.figure(figsize=(10, 5))

plt.plot(
    data.index,
    data["Close"],
    marker="o",
    label="Close Price"
)

plt.plot(
    data.index,
    data["MA5"],
    label="5-Day MA"
)

plt.plot(
    data.index,
    data["MA10"],
    label="10-Day MA"
)

plt.title(f"{ticker_symbol} Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()

plt.savefig("technical_analysis_chart.png")
print("📊 Technical analysis chart saved as technical_analysis_chart.png")

plt.show()



# Day 26: Add Volatility Analysis

data["Daily Return"] = data["Close"].pct_change()

volatility = data["Daily Return"].std() * 100
volatility_rounded = round(volatility, 2)

print("Stock Volatility:", volatility_rounded, "%")


if volatility_rounded > 3:
    print("⚠️ Risk Level: High")
elif volatility_rounded > 1:
    print("📈 Risk Level: Medium")
else:
    print("✅ Risk Level: Low")





# Add Maximum Daily Gain and Loss
max_gain = data["Daily Return"].max() * 100
max_loss = data["Daily Return"].min() * 100

print("Maximum Daily Gain:", round(max_gain, 2), "%")
print("Maximum Daily Loss:", round(max_loss, 2), "%")


# Add Sharpe Ratio (Risk vs Return Analysis)


sharpe_ratio = (
    data["Daily Return"].mean() /
    data["Daily Return"].std()
)

sharpe_ratio = round(sharpe_ratio, 2)
print("Sharpe Ratio:", sharpe_ratio)



if sharpe_ratio > 1:
    print(" Excellent Risk-Adjusted Return")
elif sharpe_ratio > 0.5:
    print(" Good Risk-Adjusted Return")
elif sharpe_ratio > 0:
    print(" Average Risk-Adjusted Return")
else:
    print(" Poor Risk-Adjusted Return")










annual_return = data["Daily Return"].mean() * 252 * 100
annual_return = round(annual_return, 2)

print("Annualized Return:", annual_return, "%")

if annual_return > 15:
    print(" Excellent Long-Term Return")
elif annual_return > 5:
    print(" Good Long-Term Return")
else:
    print(" Low Long-Term Return")

# add Dividend Information

dividends = stock.dividends

if dividends.empty:
    print(" Dividend Information: No recent dividends")
else:
    latest_dividend = dividends.iloc[-1]
    print(" Latest Dividend:", round(latest_dividend, 2))