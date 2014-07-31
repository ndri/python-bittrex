#!/usr/bin/env python
# This program buys some Dogecoins and sells them for a bigger price
from bittrex import bittrex

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('key', 'secret')

# Market to trade at
trade = 'BTC'
currency = 'DOGE'
market = '{0}-{1}'.format(trade, currency)
# Amount of coins to buy
amount = 100
# How big of a profit you want to make
multiplier = 1.1

# Getting the BTC price for DOGE
dogesummary = api.getmarketsummary(market)
dogeprice = dogesummary[0]['Last']
print 'The price for {0} is {1:.8f} {2}.'.format(currency, dogeprice, trade)

# Buying 100 DOGE for BTC
print 'Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, dogeprice, trade)
api.buylimit(market, amount, dogeprice)

# Multiplying the price by the multiplier
dogeprice = round(dogeprice*multiplier, 8)

# Selling 100 DOGE for the  new price
print 'Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, dogeprice, trade)
api.selllimit(market, amount, dogeprice)

# Gets the DOGE balance
dogebalance = api.getbalance(currency)
print "Your balance is {0} {1}.".format(dogebalance['Available'], currency)

# For a full list of functions, check out bittrex.py or https://bittrex.com/Home/Api
