#!/usr/bin/python

# This mapreduce program extract the top 10 tags weighted to the student's reputation
# that wrote the question: the higher the student's score, the higher the importance 
# given to that tag. The program combines two datasets: the users and the nodes. Since
# in the reducer's code we need all the users data before the nodes data, in the output
# of the mapper we prepend an 'A' character to the keys formed when reading the users
# file and we prepend a 'B'  character to the keys formed when reading the nodes file.

import sys
import csv

# set the reader for the TSV data file
reader = csv.reader(sys.stdin, delimiter='\t',  quotechar='"', quoting=csv.QUOTE_ALL)

# reads from TSV, record by record
for line in reader:

	# if is reading from the users file 
	# (the TSV of users has exactly 5 fields)
	if len(line) == 5:
	
		# get the id and the reputation of a student
	    student_id = line[0]
	    reputation = line[1]
	
		# a check for numeric value of student id is
		# made for skipping the header of the TSV file
	    if student_id.isdigit():
		
			# output to the reducer  the user data with the user_id and
			# a prepending "A" as the key and the reputation as the value
	        print "{0}\t{1}".format("A" + str(student_id), reputation)

	# if is reading from the node file 
	# (the TSV of nodes has exactly 19 fields)
	if len(line) == 19:

        # if this node is a question and if tags are present
		if line[5] == 'question' and len(line[2]) > 0:
			
			# get the student id
			student_id = line[3]

			# put every tag of this row into a list
			post_tags = line[2].strip().split(" ")
			
			# loop over the list of tags
			for tag in post_tags:
				
				# output to the reducer the tag prepended by a 'B' as the
				# key and id of the student as the value
				print "{0}\t{1}".format("B" + str(tag), student_id)


