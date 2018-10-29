from glob import glob
from re import sub
from collections import Counter

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
        with open(file, encoding='utf-8') as f:
            for line in f:
                yield line


def gen_grep(lines, pattern):
    for line in lines:
        if line.startswith(pattern):
            yield sub(pattern, '', line).strip()


def gen_count(lines):
    for item, count in sorted(sorted(Counter(lines).most_common(),
        reverse=True), key=lambda x:x[-1], reverse=True):
        yield f'{count:7} {item}'

'''
if __name__ == "__main__":
    files = gen_files('../*/*py')
    lines = gen_lines(files)
    lines = gen_grep(lines, 'import ')
    lines = gen_count(lines)
    for line in lines:
        print(line)
'''
