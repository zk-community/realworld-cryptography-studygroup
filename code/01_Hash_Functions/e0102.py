#!/usr/bin/env python
# coding: utf-8
# License: MIT
# Author: Chris Ward <chris@zeroknowledge.fm>

CHAPTER  = '01'
EXERCISE = '02'
NAME     = 'Encoding / Decoding Bytes'

'''
Counting Bruteforce Attacks
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

from shared import md5_digest, sha2_digest, random_ascii

# Local imports

def as_base16(string):
    # alternative: bytes(str_RAW_ASCII.encode('ascii')).hex()
    return base64.b16encode(string.encode('utf-8'))


def as_base64(string):
    return base64.b64encode(string.encode('utf-8'))


def as_md5(string):
    return md5_digest(string)


def as_bin(string, base=16, drop_prefix=True):
    bin_str = bin(int(string, base=base))
    bin_str = bin_str[2:] if drop_prefix else bin_str
    return bin_str


def as_sha2(string, depth=265):
    return sha2_digest(string, depth)


def main():
    print (__description__)
    RANDOM_SIZE = 0
    PRE_STR = "A"

    # Get our input bytes (string)
    str_RAW_ASCII = PRE_STR if not RANDOM_SIZE else random_ascii(RANDOM_SIZE)

    # Encode the string
    str_B16 = as_base16(str_RAW_ASCII)  # hexidecimal
    str_B64 = as_base64(str_RAW_ASCII)  # base64
    str_BIN = as_bin(str_B16, base=16)  # binary based from base16 encoding
    str_MD5 = as_md5(str_RAW_ASCII)
    str_SHA256 = as_sha2(str_RAW_ASCII, 256)

    print ( 'ASCII   : ', str_RAW_ASCII )
    print ( 'Bin     : ', str_BIN, f' ({len(str_BIN)} bits)')
    print ( 'B16     : ', str_B16, bytes.fromhex('41').decode('utf-8'))
    print ( 'B64     : ', str_B64 )
    print ( 'MD5     : ', str_MD5)
    print ( 'SHA256  : ', str_SHA256)


# --------------------------------------------------------------------
if __name__ == '__main__':
    main()
