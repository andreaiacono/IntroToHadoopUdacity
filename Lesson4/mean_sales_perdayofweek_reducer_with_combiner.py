#!/usr/bin/python

import sys

meanCost = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # something has gone wrong
        continue
    weekday, val = data_mapped
    #print "val=" + val + " weekday=" + weekday
    if len(val.split("|")) != 2:
    	continue
    cost, n = val.split("|")
    if not meanCost.has_key(weekday):
    	meanCost[weekday] = [float(cost), float(n)]
    else:
		meanCost[weekday] = [meanCost[weekday][0] + float(cost), meanCost[weekday][1] + float(n)]

for weekday in meanCost:
    print "{0}\t{1}".format(weekday,str(meanCost[weekday][0]/meanCost[weekday][1]) + "|" + str(meanCost[weekday][1]))

