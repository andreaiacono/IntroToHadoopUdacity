#!/usr/bin/python

# this mapreduce program extract the top10 most active students in the forums.

import sys
import csv

# dictionary that contains the student id as the key and
# and her/his score as the value
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

		# computes the score
		if line[5] == 'question':
			score = 3
		elif line[5] == 'answer':
			score = 2
		else:
			score = 1

		# if the dictionary already contains the student
		if students.has_key(student):
			
			# add the score of this node to the existing value
			students[student] += score

		# if dictionary does not contain this student
		else:

			# set the score as the new value for this student
			students[student] = score

# loop over the collected student
for student in students:

	# and output the student id and her/his score to the reducers
    print "{0}\t{1}".format(student,students[student])

