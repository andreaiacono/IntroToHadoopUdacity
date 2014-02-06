#!/usr/bin/python

# this mapreduce program indexes all the nodes by the students that posted them

import sys
import csv

# init the dictionary that will contain all the students
students = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

# loops over the input file
for line in reader:

	# if the row has 19 fields
    if len(line) == 19:

		# get the id of the node
		id = line[0]
		
		# get the id of the author of the question
		student = line[3]

		# if the dictionary already contains the student
		if students.has_key(student):
			
			# add the id of the node to the list of nodes posted by this student
			students[student].append(id)

		# if dictionary does not contain this student
		else:

			# sets the id of the node as the first element of a new list
			students[student] = [id]

# loop over the collected students
for student in students:

	# and output them to the reducers
    print "{0}\t{1}".format(student,students[student])

