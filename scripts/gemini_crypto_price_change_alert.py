# https://docs.gemini.com/rest-api/#symbols
# https://docs.gemini.com/rest-api/#price-feed

import requests, json, sys
from datetime import datetime

# Store argument as a variable 
currency = sys.argv[1]

base_url = "https://api.gemini.com/v1"

# get symbols JSON
symbols = requests.get(base_url + "/symbols").json()

# make sure the argument is valid
if currency.lower() not in symbols:
    print("Invalid currency symbol. Please select from:",symbols)
    sys.exit()

# get prices JSON
prices = requests.get(base_url + "/pricefeed").json()

# find the price block that matches the currency argument
for block in prices:
    if block['pair'] == currency.upper():
        print(datetime.now(),"- AlertingTool - INFO - Parsing args")
        print(datetime.now(),"- AlertingTool - INFO - Running check: pricechange")
        print(datetime.now(),"- AlertingTool - INFO - Running checks on currency pair:",currency)
        print(datetime.now(),"- AlertingTool - INFO - Getting symbols API Data")
        print(datetime.now(),"- AlertingTool - INFO - *** Running pricechange check on:",currency)
        print(datetime.now(),"- AlertingTool - INFO - Getting Price API Data for:",currency)
        print(datetime.now(),"- AlertingTool - INFO - Last Price:",block['price'])
        print(datetime.now(),"- AlertingTool - INFO - Price change in past 24 hours:",block['percentChange24h'])

        # Check if the current price has changed in the past 24 hours by more than 1% from the price at the start of the period
        if float(block['percentChange24h']) > .01:
            print(datetime.now(),"- AlertingTool - ALERT - ******   The price of",currency,"has changed more than 1% in the past 24 hours!")


# Instructions for running the script
# python apiAlerts.py LTCUSD (handles lower/upper cases)

# Dependencies
# python version = 3.7.5

# Further improvements
# Implement alert inputs as CLI args
# Leverage Gemini API to implement Price / Volume Deviation alerts

# Other interesting checks you might implement to alert on market behaviour
# Relevant market indicator changes like RSI, MACD

# Total time spent
# 2 hours (was trying to implement the CLI args parser / price deviation alert but didn't want to submit a half baked solution)
