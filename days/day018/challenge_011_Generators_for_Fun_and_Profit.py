from glob import glob
from re import sub

"""
Turn the following unix pipeline into Python code using generators
$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

def gen_files(pat):
    files = glob(pat)
    for file in files:
        yield file
                

def gen_lines(files):
    for file in files:
        with open(file) as f:
            yield f.readline()

def gen_grep(lines, pattern):
    for line in lines:
        yield sub(pattern, '', line)

def gen_count(lines):
    pass


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    #print(files.__next__())
    lines = gen_lines(files)
    for i in range(100):
        print(lines.__next__())
    
    '''
    grep_lines = gen_grep(lines, '(^import .*)')
    for i in range(100):
        print(grep_lines.__next__())
    '''