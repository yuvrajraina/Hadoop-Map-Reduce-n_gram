#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re

def read_input(input):
    temp=0
    for line in input:
        # split the line into words; keep returning each word
        line=line.lower()
        # all word that are not in a-z 0-9 replace them with blank space
        line=re.sub("[^a-z0-9]"," ",line)
        line=line.split()
        length=len(line)
        
        # for all 2 or 3 word inputs make them into single string by using commas
        # eg hi yuvraj ----> hi,yuvraj
        for i in range(length-1):
            temp=line[i]+','+line[i+1]
            line.append(temp)
            
        for i in range(length-2):
            temp=line[i]+','+line[i+1]+','+line[i+2]
            line.append(temp)
        yield line   
        
        


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    data=list(data)
    count=0
    
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            
            print('%s%s%d' % (word, separator, 1))
            

# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
