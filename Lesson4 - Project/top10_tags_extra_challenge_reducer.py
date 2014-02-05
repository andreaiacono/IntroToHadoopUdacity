#!/usr/bin/python

import sys
import operator

tags = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the tag and the number of times it's present in posts
    tag, score = data_mapped
	
    # if it's the first time we see this tag
    if tags.has_key(tag):
		
		# we set its value into the dictionary
		tags[tag] += int(score)

	# if the tag is already inside the dictionary
    else:
		
		# add the new value to the existing
		tags[tag] = int(score)

# sort the items by their value
sorted_tags = sorted(tags.iteritems(), key=operator.itemgetter(1))

# loop over the last 10 items (the ones that have bigger values)
for tag in sorted_tags[-10:]:
	
	# and output them
    print "{0}\t{1}".format(tag[0], tag[1])

