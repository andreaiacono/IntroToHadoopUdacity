#!/usr/bin/python

import sys

hits = {}

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 2:
		filename,value = data
		if not hits.has_key(filename):
			hits[filename] = float(value)
		else:
			hits[filename] = hits[filename] + float(value)

max = 0
hitname = ""

for filename in hits:
	if max < hits[filename]:
		max = hits[filename]
		hitname = filename

print "{0}\t{1}".format(hitname, max)
