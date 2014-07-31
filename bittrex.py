#!/usr/bin/env python
# This program buys some Dogecoins and sells them for a bigger price
from bittrex import bittrex

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('key', 'secret')

# Market to trade at
market = 'BTC-DOGE'
# Amount of coins to buy
amount = 100
# How big of a profit you want to make
multiplier = 1.1

# Getting the BTC price for DOGE
dogesummary = api.getmarketsummary(market)
dogeprice = dogesummary[0]['Last']
print 'The price for Dogecoin is {0:.8f} BTC.'.format(dogeprice)

# Buying 100 DOGE for BTC
print 'Buying {0} DOGE for {1:.8f} BTC.'.format(amount, dogeprice)
api.buylimit('BTC-DOGE', 100, dogeprice)

# Multiplying the price by the multiplier
dogeprice = round(dogeprice*multiplier, 8)

# Selling 100 DOGE for the  new price
print 'Selling {0} DOGE for {1:.8f} BTC.'.format(amount, dogeprice)
api.selllimit('BTC-DOGE', 100, dogeprice)

# Gets the DOGE balance
dogebalance = api.getbalance('DOGE')
print "Your balance is {0} DOGE.".format(dogebalance['Available'])

# For a full list of functions, check out bittrex.py or https://bittrex.com/Home/Api
