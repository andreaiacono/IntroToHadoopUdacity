#!/usr/bin/python

# this mapreduce program extract the top 10 questions that have the highest score (considering the answers/comments too). 

import sys
import csv

# dictionary that contains the question id as the key and
# and its score as the value
questions = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

# loop over the input file
for line in reader:

	# if the row has 19 fields
    if len(line) == 19:

		# get the score of this question
		score = int(line[9])
		
		# get the id of this question
		id = line[0]

		# if the dictionary already contains the question
		if questions.has_key(id):
			
			# add the score of this question to the existing value
			questions[id] += score

		# if dictionary does not contain this question
		else:

			# sets the score as the new value for this question
			questions[id] = score

# loop over the collected questions
for id in questions:

	# and output them to the reducers
    print "{0}\t{1}".format(id,questions[id])

