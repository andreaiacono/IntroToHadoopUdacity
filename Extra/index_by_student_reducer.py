#!/usr/bin/python

import sys
import ast

students = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the student and the id of the nodes she/he posted
    student, str_ids = data_mapped

	# transforms the string representation of the list
	# into a list object
    ids = ast.literal_eval(str_ids)
    
    # if the student is present in the dictionary
    if students.has_key(student):

		# adds the ids received from mapper to the existing ones
		students[student] += ids

	# if the student is not yet in the dictionary
    else:
		
		# sets the list of ids as the values for this student
		students[student] = ids

# loop over the last 10 items (the ones that have bigger values)
for student in students:
	
	# and output them
    print "{0}\t{1}".format(student, students[student])

