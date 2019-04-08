#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(", ")
    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")
    print '%s\t%s' % (words[0], 1)
