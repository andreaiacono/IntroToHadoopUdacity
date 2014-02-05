#!/usr/bin/python

import sys

words = {}

for line in sys.stdin:
	if not '\t' in line:
		continue
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
        # something has gone wrong
		continue
	word, ids = data_mapped
	if not words.has_key(word):
		words[word] = ids + ","
	else:
		words[word] += ids + ","
        
for word in words:
	print "{0}\t{1}".format(word,words[word][:len(words[word])-1])
