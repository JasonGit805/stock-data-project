import os
import pandas as pd
import sqlite3
import requests
import time

url = "https://www.alphavantage.co/query"

tickers = ["IBM", "AMZN", "GOOG", "MSFT"]
all_dfs = []
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
for ticker in tickers:
    params = {
        "function" : "TIME_SERIES_WEEKLY",
        "symbol" : ticker,
        "apikey" : API_KEY
    }
    
    time.sleep(15)
    response = requests.get(url, params = params)
    data = response.json()
    if "Weekly Time Series" not in data:
        print(f"Failed to retrieve data for {ticker}")
        print(data.keys())
        continue

    df = pd.DataFrame.from_dict(
        data['Weekly Time Series'],
        orient='index'
    )
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'date'}, inplace=True)

    df['ticker'] = ticker
    all_dfs.append(df)
if not all_dfs:
    print("No stock data retrieved.")
    exit()

final_df = pd.concat(all_dfs, ignore_index=True)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "data", "stock_data.db")
conn = sqlite3.connect(db_path)
final_df.to_sql("stocks", conn, if_exists="append", index=False)
conn.close()