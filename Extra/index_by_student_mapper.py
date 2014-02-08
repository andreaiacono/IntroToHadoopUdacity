#!/usr/bin/python

# this mapreduce program indexes all the nodes by student id

import sys
import csv

# dictionary that contains the student id as the key and
# a list of node ids as the value
students = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

# loop over the input file
for line in reader:

	# if the row has 19 fields
    if len(line) == 19:

		# get the id of the node
		id = line[0]
		
		# get the id of the author of the question
		student = line[3]

		# if the dictionary already contains the student
		if students.has_key(student):
			
			# add the id of the node to the list of node ids posted by this student
			students[student].append(id)

		# if dictionary does not contain this student
		else:

			# set the id of the node as the first element of a new list
			students[student] = [id]

# loop over the collected students
for student in students:

	# and output the student id and a list of node ids
	# (the list of node ids is formatted as the
	# string representation of a python list)
    print "{0}\t{1}".format(student,students[student])

