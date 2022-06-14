#!/usr/bin/env python
# coding: utf-8
# License: MIT
# Author: Chris Ward <chris@zeroknowledge.fm>

CHAPTER  = '01'
EXERCISE = '03'
NAME     = 'Colliding Bits'

'''
Find a collision of first 4 bits for MD5(x)
'''

__version__     = "0.1.0"
__app_name__    = f"rwc-exercise-{CHAPTER}-{EXERCISE}"
__description__ = f'RWC C{CHAPTER} E{EXERCISE}: {NAME} v{__version__}' 

import base64       # Base16, Base64
import collections  # collections. Counter
import functools    # reduce
import hashlib
import itertools    # permutations(listA)
import math         # factorial
import operator     #
import os
import sys
import string
import time

import random
random.seed()       # random.randint(a, b) random.getrandbits(k) random.randbytes(n)

from IPython.display import Image, display

# --------------------------------------------------------------------

from shared import md5_digest


class RRange:
    def __init__(self, maxsize=sys.maxsize):
        self.maxsize = maxsize
    def __iter__(self):
        return self
    def __next__(self):
        return random.randrange(0, self.maxsize)


def md5_find_collisions(target_bytes, byte_filter, max_iter, one=True):
    _md5 = md5_digest(target_bytes)
    target_nibble = _md5[:byte_filter]
    collisions = []
    for k in range(0, sys.maxsize):
        rint = next(RRange())
        e_str = str(rint).encode()
        check_md5 = md5_digest(e_str)  # _digest_bytes(e_str, hashlib.md5)
        check_nib = check_md5[:byte_filter]
        if target_nibble == check_nib:
            collisions.append((target_nibble, byte_filter, _md5, check_md5))
        if k >= max_iter or len(collisions) > 0:
            print (" ... Found one. Stopping")
            break
    return collisions


def main():
    PRE_STR = "A"

    # 2^16 == 65536, 2^17 == 131072, 2^18 == 262144
    max_iter = int(math.pow(2, 25))

    s_ts = time.perf_counter()  # start timer
    collisions = md5_find_collisions(PRE_STR, 4, max_iter)

    e_ts = time.perf_counter()  # end timer
    print ( 'Finished in {:0.4f}s'.format(float((e_ts - s_ts))) )
    print (f'Collisions: {len(collisions)} (max_iter: {max_iter})')
    for i, c in enumerate(collisions):
        print (f'{i} : {c[0]} < {c[1]} >>\n{c[2]}\n{c[3]}')


# --------------------------------------------------------------------
if __name__ == '__main__':
    main()
