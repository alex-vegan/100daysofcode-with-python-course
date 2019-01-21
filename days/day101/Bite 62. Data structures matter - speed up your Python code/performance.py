from functools import wraps
from time import time
from typing import List, Set
import random
from string import ascii_lowercase


def timing(f):
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        duration = end - start
        print(f'Elapsed time {f.__name__}: {duration}')
        return duration, result
    return wrapper


@timing
def contains(sequence: List[int], num: int) -> bool:
    for n in sequence:
        if n == num:
            return True
    return False


@timing
def contains_fast(sequence: Set[int], num: int) -> bool:
    return sequence.issuperset({num})


@timing
def ordered_list_max(sequence: List[int]) -> int:
    return max(sequence)


@timing
def ordered_list_max_fast(sequence: List[int]) -> int:
    return max(sequence[0], sequence[-1])


@timing
def list_concat(sequence: List[str]) -> str:
    bigstr = ''
    for i in sequence:
        bigstr += str(i)
    return bigstr


@timing
def list_concat_fast(sequence: List[str]) -> str:
    return ''.join(sequence)


@timing
def list_inserts(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.insert(0, i)
    return lst


@timing
def list_inserts_fast(n: int) -> List[int]:
    lst = []
    for i in range(n-1, -1, -1):
        lst.append(i)
    return lst


@timing
def list_creation(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


@timing
def list_creation_fast(n: int) -> List[int]:
    return list(range(n))


if __name__ == "__main__":
    alist = range(1000000)
    aset = set(alist)
    aint = random.choice(range(1000000))
    astr = list(ascii_lowercase) * 1000
    #print(contains(alist, 123456))
    #print(contains_fast(aset, 123456))
    #print(ordered_list_max(alist))
    #print(ordered_list_max_fast(alist))
    #list_concat(astr)
    #list_concat_fast(astr)
    #list_inserts(10000)
    #list_inserts_fast(10000)
    #list_creation(10000)
    #list_creation_fast(10000)
