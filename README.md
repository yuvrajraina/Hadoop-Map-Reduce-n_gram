# Hadoop-Map-Reduce-n_gram
Hadoop map reduce for solving n gram problems


The submission was programmed in python and tested on peel system.
To run the code:
    mapred streaming -input <testfile> -output <outputfile> -mapper "python mapper.py" -reducer "python reducer.py" -file mapper.py -file reducer.py
    this should run and output will be stored as <outputfile>
use this file and run:
    mapred streaming -input <outputfile> -output <finalfile> -mapper "python mapper2.py" -reducer "python reducer2.py" -file mapper2.py -file reducer2.py
    
xxxxxxxxxxxx    make sure that <outputfile> was stored as .txt final file will only need parsing xxxxxxxxxx

parse using, 
hdfs dfs -cat <outputfile>.txt/par*
this should parse output.

In output if you notice a lot of: 

----- 0/n   ------ 0/n-1    word is here 1/n-2

do not be surprised it has been formatted that way so that non empty elements look good in the column if one column exceeds in width,

here n is the number of occurances of unigram elements.
