#!/usr/bin/python

import sys

no_sales = 0
total_cost = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) == 2:
		ns, tc = data_mapped
		no_sales = no_sales + float(ns)
		total_cost = total_cost + float(tc) 

print "{0}\t{1}\n".format(no_sales,total_cost)
