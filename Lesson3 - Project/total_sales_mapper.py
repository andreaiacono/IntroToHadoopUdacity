#!/usr/bin/python

import sys

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

no_sales = 0
total_cost = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        total_cost = total_cost + float(cost)
        no_sales = no_sales +1
		
print "{0}:\t{1}\n".format(no_sales,total_cost)

