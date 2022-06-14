#!/usr/bin/env python
# coding: utf-8
# License: MIT
# Author: Chris Ward <chris@zeroknowledge.fm>

CHAPTER  = '01'
EXERCISE = '01'
NAME     = ''  # Title

# Description
'''
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



def main():
    print (__description__)


# --------------------------------------------------------------------
if __name__ == '__main__':
    main()
