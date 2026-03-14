import requests
import json

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum"
}

response = requests.get(url, params=params)

data = response.json()

crypto_data = []

for coin in data:
    coin_info = {
        "name": coin["name"],
        "symbol": coin["symbol"],
        "price": coin["current_price"],
        "market_cap": coin["market_cap"]
    }

    crypto_data.append(coin_info)

with open("crypto_data.json", "w") as file:
    json.dump(crypto_data, file, indent=4)

print("Crypto data saved successfully!")