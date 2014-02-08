#!/usr/bin/python

# this mapreduce program indexes the questions by tags

import sys
import csv

# dictionary that contains the tag as the key and
# a list of node ids (that contain that tag) as the value
tags = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

# loop over the input file
for line in reader:

	# if the row has 19 fields
    if len(line) == 19:

        # if this node is a question and if tags are present
		if line[5] == 'question' and len(line[2]) > 0:
			
			# get the id of the question
			id = line[0]

			# put every tag of this row into a list
			post_tags = line[2].split(" ")
			
			# loop over the list of tags
			for tag in post_tags:
				
				# if the dictionary already contains the tag
				if tags.has_key(tag):
					
					# add the score of this question to the existing value
					tags[tag].append(id)

				# if dictionary does not contain this tag
				else:

					# set the score as the new value for this tag
					tags[tag] = [id]

# loop over the collected tags
for tag in tags:

	# and output them to the reducers
    print "{0}\t{1}".format(tag,tags[tag])

