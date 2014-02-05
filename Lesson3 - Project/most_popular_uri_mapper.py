#!/usr/bin/python

import re
import sys

count = 0
regex = '([(\d\.)]+) ([\S]*) (.*) \[(.*)\] "(.+)" (\d+) (.*)$'
hits = {}

for line in sys.stdin:
	filename = re.match(regex, line).groups()[4]
	pos = filename.find(" ")
	filename = filename[pos+1:]
	pos = filename.find(" ")
	filename = filename[:pos]
	if not hits.has_key(filename):
		hits[filename] = 1
	else:
		hits[filename] = hits[filename] + 1

for filename in hits:
    print "{0}\t{1}".format(filename,hits[filename])

