#!/usr/bin/python

import sys

words = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # something has gone wrong
        continue
    word, count = data_mapped
    if not words.has_key(word):
        words[word] = float(count)
    else:
        words[word] += float(count)
        
for word in words:
    print "{0}\t{1}\n".format(word,words[word])
