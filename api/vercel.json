import json
import requests
from datetime import datetime

def handler(request):
    funding = requests.get(
        "https://fapi.binance.com/fapi/v1/fundingRate",
        params={"symbol": "BTCUSDT", "limit": 1}
    ).json()[0]

    funding_rate = float(funding["fundingRate"])
    timestamp = datetime.utcnow().isoformat()

    signal = "NEUTRAL"
    if funding_rate > 0:
        signal = "SHORT"
    elif funding_rate < 0:
        signal = "LONG"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "timestamp": timestamp,
            "funding_rate": funding_rate,
            "signal": signal
        })
    }
