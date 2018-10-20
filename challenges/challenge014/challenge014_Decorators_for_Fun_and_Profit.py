from glob import glob
from re import sub
from collections import Counter
from functools import wraps
from time import time_ns


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
#-------------------------------------------------------------------------------
def timeit(func):
    '''decorator for check time of func execution'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time_ns()
        result = func(*args, **kwargs)
        end = time_ns()
        print(f'funtion "{func.__name__}" executed about {end-start} nanoseconds')
        return result
    return wrapper

#-------------------------------------------------------------------------------
@timeit
def gen_files(pat):
    files = glob(pat)
    for file in files:
        yield file

@timeit
def fun_files(pat):
    files = glob(pat)
    return files

#-------------------------------------------------------------------------------
@timeit
def gen_lines(files):
    for file in files:
        with open(file, encoding='utf-8') as f:
            for line in f:
                yield line

@timeit
def fun_lines(files):
    lines = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            lines.extend(f.readlines())
    return lines

#-------------------------------------------------------------------------------
@timeit
def gen_grep(lines, pattern):
    for line in lines:
        if line.startswith(pattern):
            yield sub(pattern, '', line).strip()

@timeit
def fun_grep(lines, pattern):
    grep_lines = []
    for line in lines:
        if line.startswith(pattern):
            grep_lines.append(sub(pattern, '', line).strip())
    return grep_lines

#-------------------------------------------------------------------------------
@timeit
def gen_count(lines):
    for item, count in sorted(sorted(Counter(lines).most_common(),
        reverse=True), key=lambda x:x[-1], reverse=True):
        yield f'{count:7} {item}'

@timeit
def fun_count(lines):
    count_list = []
    for item, count in sorted(sorted(Counter(lines).most_common(),
        reverse=True), key=lambda x:x[-1], reverse=True):
        count_list.append(f'{count:7} {item}')
    return '\n'.join(count_list)

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    print('compare exec time of generators and functions by using decorator')
    print('-'*101)
    files = gen_files('../*/*py')
    lines = gen_lines(files)
    lines = gen_grep(lines, 'import ')
    lines = gen_count(lines)
    for line in lines:
        print(line)
    print('-'*101)
    files = fun_files('../*/*py')
    lines = fun_lines(files)
    lines = fun_grep(lines, 'import ')
    lines = fun_count(lines)
    print(lines)
    print('-'*101)
