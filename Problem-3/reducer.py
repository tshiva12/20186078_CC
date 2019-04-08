#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            temp = [current_word, current_count]
            print '%s' %(temp)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    final_temp = [current_word, current_count]
    print '%s' % (final_temp)
