#!/usr/bin/python

import re
import sys

count = 0
regex = '([(\d\.)]+) ([\S]*) (.*) \[(.*)\] "(.+)" (\d+) (.*)$'
searched_uri = '/assets/js/the-associates.js'

for line in sys.stdin:
	uri = re.match(regex, line).groups()[4]
	if searched_uri in uri:
		count = count +1

print "{0}\t{1}".format(searched_uri, count)
