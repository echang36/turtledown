#!/usr/bin/env python

import sys

#input comes from STDIN (standard input)
for line in sys.stdin:

	line=line.strip()
	words=line.split()
	
	for word in words:
		#write the results to STDOUT (standard output)
		print '%s\t%s' %(word,1)