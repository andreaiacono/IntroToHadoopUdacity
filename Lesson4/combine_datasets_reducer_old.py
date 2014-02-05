# Here you will be able to combine the values that come from 2 sources
# Value start starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

users = {}

def reducer():
    
	# reads data from mapper as CSV because of newlines inside body
	reader = csv.reader(sys.stdin, delimiter='\t',  quotechar='"', quoting=csv.QUOTE_ALL)
	for line in reader:

		# the first field is the user id, whatever the type of record (user or node)
		user_id = line[0]

		# if we're receiving a user row
		if line[1][0] == 'A':

			# add it to the dictionary (removing the 'A' character from the second field)
			users[user_id] = [line[1][1:], line[2], line[3], line[4]]

		# if we're receiving a node row
		elif line[1][0] == 'B':
			
			# we take the user_id, the second field (removing the 'B' character)
			row = [line[0], line[1][1:]]
			
			# and add all the other fields of the node
			for i in range(2,19):
				row.append(line[i])
	
			# now we add the fields of the user
			row.extend(users[user_id])

			# and print the complete data of the node and the user who has posted it
			print row

def main():
    reducer()

main()