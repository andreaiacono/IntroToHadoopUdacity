#!/usr/bin/python

import re
import sys

count = 0
regex = '([(\d\.)]+) ([\S]*) (.*) \[(.*)\] "(.+)" (\d+) (.*)$'
searched_ip = '10.99.99.186'

for line in sys.stdin:
	ip = re.match(regex, line).groups()[0]
	if searched_ip in ip:
		count = count +1

print "{0}\t{1}".format(searched_ip, count)
