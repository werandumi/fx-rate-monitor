import json
import requests
from datetime import datetime

url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
payload = {
    "asset": "USDT",
    "fiat": "TZS",
    "tradeType": "BUY",
    "payTypes": ["crdb", "nmb", "BANK", "EquityBank", "CashDeposit"],
    "page": 1,
    "rows": 10,
    "merchantCheck": False
}
response = requests.post(url, json=payload)
response.raise_for_status()
data = response.json()
ads=data["data"]

print(f"\nUSDT/TZS sell ads — banks only — {datetime.now():%Y-%m-%d %H:%M}\n")

for i, item in enumerate(ads, start=1):
    adv = item["adv"]                                     # ad: price, quantity, methods
    advertiser = item["advertiser"]                       # merchant

    price = adv["price"]
    name = advertiser["nickName"]
    available = adv["tradableQuantity"]
    finish_rate = float(advertiser["monthFinishRate"]) * 100

    print(f"{i}. {price} TZS | {name} | {available} USDT left | {finish_rate:.1f}% completion")