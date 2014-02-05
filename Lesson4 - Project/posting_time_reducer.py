#!/usr/bin/python

import sys
import ast

# the dictioanry in which we'll write for each user all the post 
# for each hour
users = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the id of the user and the dictionary as a string
    id, hours_str = data_mapped
	
	# transforms the string representation of the dictionary
	# into a real dictionary
    hours = ast.literal_eval(hours_str)
    
	# if it's the first time we see this user, we assign to it 
	# the dictionary
    if not users.has_key(id):
    	users[id] = hours

	# if we already have this user
    else:

		# for every hour in the dictionary got from mapper
        for hour in hours:

			# if the user already has set the number of posts for
			# this hour, increases its value by the value got 
			# got from mapper
			if users[id].has_key(hour):
				users[id][hour] += hours[hour]

			# else simply sets the the number of posts as the value
			# got from mapper
			else:
				users[id][hour] = hours[hour]

# loops in users dictionary
for user in users:

	# sets local variables for finding the max number of posts
	# for every user
    max_hour = 0
    hour_index = 0

	# loops the hours for this user for finding the max
    for hour in users[user]:
        if users[user][hour] > max_hour:
            max_hour = users[user][hour]
            hour_index = hour

	# and outputs the id of the user and the hour in which he/she 
	# has written the maximum number of posts
    print "{0}\t{1}".format(user,hour_index)

