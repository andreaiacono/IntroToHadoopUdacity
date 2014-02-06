#!/usr/bin/python

import sys
import operator

students = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the tag and the number of times it's present in posts
    student, score = data_mapped
	
    # if it's the first time we see this student
    if students.has_key(student):
		
		# we set its value into the dictionary
		students[student] += int(score)

	# if the student is already inside the dictionary
    else:
		
		# add the new value to the existing
		students[student] = int(score)

# sort the items by their value
sorted_students = sorted(students.iteritems(), key=operator.itemgetter(1))

# loop over the last 10 student (the ones that have the highest scores)
for student in sorted_students[-10:]:
	
	# and output them
    print "{0}\t{1}".format(student[0], student[1])

