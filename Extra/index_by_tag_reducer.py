#!/usr/bin/python

import sys
import ast

tags = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the tag and the number of times it's present in posts
    tag, str_ids = data_mapped

	# transforms the string representation of the list
	# into a list object
    ids = ast.literal_eval(str_ids)
    
    # if it's the first time we see this tag
    if tags.has_key(tag):

		# adds the ids received from mapper to the existing ones		
		tags[tag] += ids

	# if the tag is already inside the dictionary
    else:
		
		# add the new value to the existing
		tags[tag] = ids

# loop over the last 10 items (the ones that have bigger values)
for tag in tags:
	
	# and output them
    print "{0}\t{1}".format(tag, tags[tag])

