#!/usr/bin/python

# this mapreduce program extract the top10 tags weighted to the student's score that wrote the question: the higher the student's score, the higher the importance given to that tag.

import sys
import csv

# init the dictionary that will contain all the tags
tags = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

# loops over the input file
for line in reader:

	# if the row has 19 fields
    if len(line) == 19:

        # if this node is a question and if tags are present
		if line[5] == 'question' and len(line[2]) > 0:
			
			# put every tag of this row into a list
			post_tags = line[2].split(" ")
			
			# gets the score of this post
			score = int(line[9])
			
			# loop over th elist of tags
			for tag in post_tags:
				
				# if the dictionary already contains the tag
				if tags.has_key(tag):
					
					# add the score of this question to the existing value
					tags[tag] += score

				# if dictionary does not contain this tag
				else:

					# sets the score as the new value for this tag
					tags[tag] = score

# loop over the collected tags
for tag in tags:

	# and output them to the reducers
    print "{0}\t{1}".format(tag,tags[tag])

