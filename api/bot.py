import requests
import json

def main(request):
    funding = requests.get(
        "https://fapi.binance.com/fapi/v1/fundingRate",
        params={"symbol": "BTCUSDT", "limit": 1}
    ).json()[0]

    rate = float(funding["fundingRate"])

    signal = "LONG" if rate < 0 else "SHORT"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "funding_rate": rate,
            "signal": signal
        })
    }
