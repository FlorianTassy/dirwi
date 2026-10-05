import json
from urllib.request import urlopen

URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

def get_btc_price():
    with urlopen(URL, timeout=10) as response:
        data = json.load(response)
    return float(data["data"]["amount"])
