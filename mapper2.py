from itertools import groupby
from operator import itemgetter
import sys
import re
import json

def read_input(input):
    separator='\t'
    length=0
    for line in input:
        # split the line into words; keep returning each word and its value
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    # careful input in generator format
    # currently the current_word contains both the element and count no need for itemgetter
    # as there is onle on word value pair bcoz reducer has already reduced values to single key pair
    for current_word, group in groupby(data):
        try:
            
            # return value in processible json format ["word","count"]
            # make sure value not in format ['word','count]
            # this is not readable for json so use the first one
            # hard coded the format as normal method would return in 2nd format
            print('allforone%s["%s","%s"]' % (separator,current_word[0],current_word[1]))
            
            #to test not iterating again theory
            #print("%s%s%s" % (current_word[0], separator, current_word[1]))
        except ValueError:
            
            pass
    
    
            
    
    
# how to test locally in bash/linus: cat <input> | python mapper2.py
if __name__ == "__main__":
    main()
