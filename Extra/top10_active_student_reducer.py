#!/usr/bin/python

import sys
import operator

# dictionary that contains the student id as the key and
# and her/his score as the value
students = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divide the line using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields
    if len(data_mapped) != 2:

        # just skip this line
        continue

	# get the student id and her/his score
    student, score = data_mapped
	
    # if the dictionary already contains the student
    if students.has_key(student):
		
		# add the new value to the existing
		students[student] += int(score)

	# if dictionary does not contain this student
    else:
		
		# set its value into the dictionary
		students[student] = int(score)

# sort the students by their score
sorted_students = sorted(students.iteritems(), key=operator.itemgetter(1))

# loop over the last 10 student (the ones that have the highest scores)
for student in sorted_students[-10:]:
	
	# and output them as student id and her/his score
    print "{0}\t{1}".format(student[0], student[1])

