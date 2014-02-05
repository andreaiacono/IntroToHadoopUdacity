#!/usr/bin/python

import sys
import ast

posts = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the id of the post and the rest of the data
    id, data = data_mapped
	
	# splits the data into the three variables
    post_length, answers_length, number_of_answers = data.strip().split("|")

	# if isn't the first time we see this post
    if posts.has_key(id):
		
		# we update its values with the ones just received
		posts[id] = [posts[id][0] + int(post_length), posts[id][1] + int(answers_length), posts[id][2] + int(number_of_answers)]

	# first time for this post
    else:
		# init array and sets values
		posts[id] = []
		posts[id] = [int(post_length), int(answers_length), int(number_of_answers)]

# loops over the posts
for id in posts:
	
	# if this post has answers
	if posts[id][2] > 0:

		# outputs the desired info
		print "{0}\t{1}".format(id,str(posts[id][0]) + "|" + str(posts[id][1] / posts[id][2]))


