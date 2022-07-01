#!/bin/python

from coin_price_extractor import CoinPriceExtractor
from prometheus_client import Gauge, start_http_server
from time import sleep, time

print("Coin Market Cap data exporter")
print("For dumping to Prometheus")

start_http_server(8000) # Start http server to show metrics

gauges = {} # All gauge data cache. key=currency_name, value=gauge


coin_extractor = CoinPriceExtractor(None)

while True:
    data = coin_extractor.extract(1)

    for currency_name, currency_price in data.items():
        currency_name = "price_"+currency_name.replace("-", "_")
        if currency_name not in gauges:
            gauges[currency_name] = Gauge(
                currency_name, currency_name + ' price')

        gauges[currency_name].set(currency_price)
    
    sleep(10)
