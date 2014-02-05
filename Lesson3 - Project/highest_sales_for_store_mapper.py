#!/usr/bin/python

import sys

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

highestCost = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        if not highestCost.has_key(store):
            highestCost[store] = float(cost)
        else:
            if highestCost[store] < float(cost):
				highestCost[store] = float(cost)

for store in highestCost:
    print "{0}:\t{1}\n".format(store,highestCost[store])

