import pandas as pd
import json
import matplotlib.pyplot as plt
from datetime import datetime

with open(r'C:\Users\liamn\Downloads\sample.json') as f:
    data = json.load(f)

# Use pd.json_normalize to convert the JSON to a DataFrame
df = pd.json_normalize(data['stocks'], meta=["ticker", "volume", "v-weight-price", "open", "close", "high", "low", "date"])
# Rename the columns for clarity
df.columns = ["ticker", "volume", "v-weight-price", "open", "close", "high", "low", "date"]

df["date"] = pd.to_datetime(df["date"])

df.set_index("date")

#create figure
plt.figure()

#define width of candlestick elements
width = .4
width2 = .05

#define up and down prices
up = df[df.close>=df.open]
down = df[df.close<df.open]

#define colors to use
col1 = 'green'
col2 = 'red'

#plot up prices
plt.bar(up.index,up.close-up.open,width,bottom=up.open,color=col1)
plt.bar(up.index,up.high-up.close,width2,bottom=up.close,color=col1)
plt.bar(up.index,up.low-up.open,width2,bottom=up.open,color=col1)

#plot down prices
plt.bar(down.index,down.close-down.open,width,bottom=down.open,color=col2)
plt.bar(down.index,down.high-down.open,width2,bottom=down.open,color=col2)
plt.bar(down.index,down.low-down.close,width2,bottom=down.close,color=col2)

#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')

plt.xlabel("Date")
plt.ylabel("Price")

#display candlestick chart
plt.show()

# Display the DataFrame
# print(df)
df.to_csv()
