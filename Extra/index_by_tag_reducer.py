#!/usr/bin/python

import sys
import ast

# dictionary that contains the tag as the key and
# a list of node ids (that contain that tag) as the value
tags = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divide the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields
    if len(data_mapped) != 2:

        # just skip this line
        continue

	# get the tag and the list of node ids in which is present
    tag, str_ids = data_mapped

	# transform the string representation of the list
	# into a list object
    ids = ast.literal_eval(str_ids)
    
    # if the dictionary contains this tag
    if tags.has_key(tag):

		# add the ids received from mapper to the existing ones		
		tags[tag] += ids

	# if the tag is not inside the dictionary
    else:
		
		# add the new value to the existing
		tags[tag] = ids

# loop over the tags
for tag in tags:
	
	# and output them (the list of node ids is formatted as the
	# string representation of a python list)
    print "{0}\t{1}".format(tag, tags[tag])

