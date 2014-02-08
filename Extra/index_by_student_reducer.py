#!/usr/bin/python

import sys
import ast

# dictionary that contains the student id as the key and
# a list of node ids as the value
students = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divide the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields
    if len(data_mapped) != 2:

        # just skip this line
        continue

	# get the student and the id of the nodes she/he posted
    student, str_ids = data_mapped

	# transform the string representation of the list
	# into a list object
    ids = ast.literal_eval(str_ids)
    
    # if the student is present in the dictionary
    if students.has_key(student):

		# add the ids received from mapper to the existing ones
		students[student] += ids

	# if the student is not yet in the dictionary
    else:
		
		# set the list of ids as the values for this student
		students[student] = ids

# loop over students
for student in students:
	
	# and output them (the list of node ids is formatted as the
	# string representation of a python list)
    print "{0}\t{1}".format(student, students[student])

