import requests
url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
payload = {
    "asset": "USDT",
    "fiat": "TZS",
    "tradeType": "SELL",
}
response = requests.post(url, json=payload)
response.raise_for_status()
data = response.json()
print(data)