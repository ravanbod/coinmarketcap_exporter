# coinmarketcap_exporter
A prometheus coinmarketcap exporter (Just for fun)

# What is it?
This project collects data from coinmarketcap.com and stores them in the Prometheus.

# How can I run it?
All you have to do is running `docker-compose up -d` and open `localhost:9090`.

You can search `price_bitcoin` or another coin in the query field of prometheus and see the price changes.

# How does it collect data?
It collects data using `bs4` module.

# Attention
I will not update this project. This was a homework of a course in my university :)
