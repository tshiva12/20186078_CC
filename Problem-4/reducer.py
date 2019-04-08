#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

friends_dict = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(", ")

    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")

    words[1] = words[1].strip("]")
    words[1] = words[1].strip("\"")
    
    if words[0] not in friends_dict.keys():
        friends_dict[words[0]] = [words[1]]
    else:
        friends_dict[words[0]].append(words[1])


# print friends_dict


dict2 = friends_dict.copy()

# print "After update"

li = friends_dict.keys()

# print li

for i in li:
    for j in friends_dict[i]:
        if j in li:
            if i in friends_dict[j]:
                friends_dict[j].remove(i) 
                friends_dict[i].remove(j)

for k in friends_dict.keys():
    for l in friends_dict[k]:
        print [l, k]
        print [k ,l]            
