#!/usr/bin/python

import sys
import operator

# dictionary that contains the question id as the key and
# and its score as the value
questions = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divide the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields
    if len(data_mapped) != 2:

        # just skip this line
        continue
	
	# get the question id and its score
    id, score = data_mapped
	
    # if the question is already inside the dictionary
    if questions.has_key(id):
		
		# add the new value to the existing
		questions[id] += int(score)

	# if dictionary does not contain this question
    else:
		
		# set its value into the dictionary
		questions[id] = int(score)

# sort the questions by their score
sorted_questions = sorted(questions.iteritems(), key=operator.itemgetter(1))

# loop over the last 10 question (the ones that have biggest score)
for id in sorted_questions[-10:]:
	
	# and output as question id and its score
    print "{0}\t{1}".format(id[0], id[1])

