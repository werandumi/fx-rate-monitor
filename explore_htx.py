import requests
from datetime import datetime

htx_url = "https://www.htx.com/-/x/otc/v1/data/trade-market"

params = {
    "coinId": 2,            # USDT
    "currency": 172,        # CNY's numeric ID
    "tradeType": "buy",       
    "currPage": 1,
    "pageSize": 5,
    "payMethod": "2,3",     # Alipay and WeChat
    "blockType": "general",
    "online": 1,
    "range": 0,
    "amount": 5000,         # 5000 RMB filter
    "onlyTradable": "false",
}

response = requests.get(htx_url, params=params,
                        headers={"User-Agent": "Mozilla/5.0"})
response.raise_for_status()
data = response.json()
ads = data["data"]

print(f"\nUSDT/CNY buy ads — Alipay and WeChat — {datetime.now():%Y-%m-%d %H:%M}\n")

for i, ad in enumerate(ads, start=1):
    price = ad["price"]
    name = ad["userName"]
    available = float(ad["tradeCount"])
    finish_rate = float(ad["orderCompleteRate"])

    print(f"{i}. {price} CNY | {name} | {available:.1f} USDT left | {finish_rate:.1f}% completion")