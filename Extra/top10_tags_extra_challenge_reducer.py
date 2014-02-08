#!/usr/bin/python

import sys
import operator
import csv

# dictionary that contains the student id as the key and 
# her/his reputation as the value
student = {}

# dictionary that contains the tag as the key and 
# its score as value
tags = {}

# set the reader for the TSV data file
reader = csv.reader(sys.stdin, delimiter='\t',  quotechar='"', quoting=csv.QUOTE_ALL)

# read from the output of mappers
for line in reader:
	
	# if there are only two fields
	if len(line) == 2:

		# if we're receiving a user 
		# (check on the first char of the key)
		if line[0][0] == 'A':

			# get the student id removing the prepending 'A'
			student_id = line[0][1:]

			# get the reputation
			reputation = int(line[1])
			
			# add the student's reputation to the dictionary
			student[student_id] = reputation

		# if we're receiving a tag
		# (check on the first char of the key)
		elif line[0][0] == 'B':

			# get the tag removing the prepending 'B'
			tag = line[0][1:]

			# get the student id 
			student_id = line[1]
			
			# defensive check
			# if student_id is not in the dictionary
			if not student.has_key(student_id):
			
				# it means the data of user and nodes is not coherent because
				# in nodes file are present nodes that have an author_id that 
				# is not present in the users file. So just skip it.
				continue;

			# if the dictionary contains the tag			
			if tags.has_key(tag):
				
				# increment by the reputation of the student this tag
				tags[tag] += student[student_id]
			
			# if the dictionary does not contain the tag
			else:
				
				# set the reputation of the student as the tag value
				tags[tag] = student[student_id]

# sort the tags by their score
sorted_tags = sorted(tags.iteritems(), key=operator.itemgetter(1))

# loop over the last 10 tags (the ones that have highest scores)
for tag in sorted_tags[-10:]:
	
	# and output the tag and its score
    print "{0}\t{1}".format(tag[0], tag[1])

