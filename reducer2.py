#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys
import re
import json

# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)

# ['unary','['word','
def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    temp = data
    count_unigram=0
    count_bigram=0
    count_trigram=0
    word_list_trigram=[]
    word_list_unigram=[]
    word_list_bigram=[]
    # group contains both word and count
    # hard coded so as to not let the reducer be more than one
    # append elements to respected n gram lists
    # word in format '["word","value"]' convert to list using the json loads method included default
    print('unigram                                       bigram                                             trigram')
    
    for current_word,group in groupby(data,itemgetter(0)):
        try:    
            for current,word in group:
                
                word=json.loads(word)
                if len(re.findall(',',word[0]))==2:
                    word_list_trigram.append(word)
                    
                    
                elif len(re.findall(',',word[0]))==1:
                    word_list_bigram.append(word)
                    
                else:
                    word_list_unigram.append(word)
                    count_unigram=int(word[1])+count_unigram          
            # find max length and min length of the arrays
            # now subtract the elements size from max and min to get how many empty spaces
            # to add for formatting a clean and clear table sortof structure
            # replace all comma separator with spaces to get original words     
            count_trigram = count_unigram -2
            count_bigram = count_unigram-1   
            max_len = max(len(word_list_trigram), len(word_list_bigram), len(word_list_unigram))
            min_len = min(len(word_list_trigram), len(word_list_bigram), len(word_list_unigram))
            val_diff= max_len-min_len
            val_emp =["----","0"]
            for i in range(val_diff):
                word_list_unigram.append(val_emp)
                word_list_bigram.append(val_emp)
                word_list_trigram.append(val_emp)
            for i in range(max_len):
                print('%s%s%s/%s%s%s%s%s/%s%s%s%s%s/%s' % (word_list_unigram[i][0].replace(',',' '), separator, word_list_unigram[i][1],count_unigram,separator,word_list_bigram[i][0].replace(',',' '),separator,word_list_bigram[i][1],count_bigram,separator,word_list_trigram[i][0].replace(',',' '),separator,word_list_trigram[i][1],count_trigram))
                
        except ValueError:
            # count was not a number, so silently discard this item
            pass
           
    
if __name__ == "__main__":
    main()
