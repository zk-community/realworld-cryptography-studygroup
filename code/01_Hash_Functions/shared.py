#!/usr/bin/env python
# coding: utf-8
# License: MIT
# Author: Chris Ward <chris@zeroknowledge.fm>

CHAPTER  = '01'
EXERCISE = 'shared'
NAME     = 'Demonstrate one or more attacks on MD5'

__version__     = "0.1.0"
__app_name__    = f"rwc-exercise-{CHAPTER}-{EXERCISE}"
__description__ = f'RWC C{CHAPTER} E{EXERCISE}: {NAME} v{__version__}' 

import hashlib
import os

from IPython.display import Image, display
# --------------------------------------------------------------------


def digest_bytes(str_bytes, lib):
    # str_bytes is expected to be encoded already
    _hash = lib()
    _hash.update(str_bytes)
    _digest = _hash.hexdigest()
    return _digest


def digest(_input, lib):
    # Overwrite _input with file bytes if we have a valid path
    if os.path.exists(_input):
        with open(_input, "rb") as _file:
            str_bytes = _file.read()
    else:
        try:
            str_bytes = _input.encode('ascii')
        except AttributeError:
            str_bytes = _input  # already encoded
    return digest_bytes(str_bytes, lib)


def md5_digest(filepath):
    return digest(filepath, hashlib.md5)


def sha2_digest(filepath, depth=256):
    return digest(filepath, hashlib.sha256)


def random_ascii(chars_len):
    # 8bit ASCII encoding: 1 char = 8 bits or 1 byte
    encoding = string.ascii_letters
    r = lambda: random.randint(0, len(char_set) - 1)
    return ''.join([encoding[r()] for _ in range(chars_len)])


# Calculate how many operations for all permutations
def npermutations(l):
    num = math.factorial(len(l))
    mults = collections.Counter(l).values()
    den = functools.reduce(operator.mul, (math.factorial(v) for v in mults), 1)
    return num / den
