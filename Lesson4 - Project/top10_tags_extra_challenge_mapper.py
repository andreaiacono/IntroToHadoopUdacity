#!/usr/bin/python

import sys
import csv

tags = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

for line in reader:
	# if the row has 19 fields
    if len(line) == 19:

        # get the tags
		if len(line[2]) > 0:
			
			post_tags = line[2].split(" ")
			
			# gets the score of this post
			score = int(line[9])
			
			for tag in post_tags:
				
				if tags.has_key(tag):
					tags[tag] += score
				else:
					tags[tag] = score

for tag in tags:
    print "{0}\t{1}".format(tag,tags[tag])
