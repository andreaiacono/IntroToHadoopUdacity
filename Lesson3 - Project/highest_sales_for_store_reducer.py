#!/usr/bin/python

import sys

highestCost = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # something has gone wrong
        continue
    store, cost = data_mapped
    if not highestCost.has_key(store):
        highestCost[store] = float(cost)
    else:
        if highestCost[store] < float(cost):
            highestCost[store] = float(cost)

for store in highestCost:
    print "{0}\t{1}\n".format(store,highestCost[store])
