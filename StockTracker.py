import requests
import pandas
import matplotlib.pyplot as plt

# Read the API key from a file to keep it secure
with open("stock_api_key.txt", "r") as f:
    api_key = f.read().strip()

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&symbol=AAPL&apikey={api_key}"
response = requests.get(url)
data = response.json()

df = pandas.DataFrame(data["Time Series (Daily)"]).T.sort_index().tail(30)
df = df.astype(float)
df = df.reset_index()
df = df.rename(columns={"index": "Date", "1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"})

closing_prices = df['Close']
average_closing_price = closing_prices.mean()
print("Average Closing Price:", average_closing_price)

for day in df.values:
    print(day[0], float(day[4] - day[1]))

plt.plot(df['Date'], df['Close'], color='blue')
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.ylabel("Closing Price (USD)")
plt.title("Apple (AAPL) Closing Prices Over the Past Month")
plt.show()

# Analysis of stock closing prices:
# There was a steep drop on 9/12 which rebounded on 9/16 - 9/18
# The stock remained steady with a slight increase from 9/18 - 9/26
# Then there were 2 steep drops which ended on 10/4 with another rebound that is still increasing