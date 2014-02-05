#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 2:
		uri,value = data
		count = count + float(value)

print "{0}\t{1}".format(uri, count)
