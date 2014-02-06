#!/usr/bin/python

import sys
import operator

questions = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the question id and its score
    id, score = data_mapped
	
    # if the question is already inside the dictionary
    if questions.has_key(id):
		
		# add the new value to the existing
		questions[id] += int(score)

	# if it's the first time we see this question
    else:
		
		# we set its value into the dictionary
		questions[id] = int(score)

# sort the questions by their score
sorted_questions = sorted(questions.iteritems(), key=operator.itemgetter(1))

# loop over the last 10 items (the ones that have bigger values)
for id in sorted_questions[-10:]:
	
	# and output them
    print "{0}\t{1}".format(id[0], id[1])

