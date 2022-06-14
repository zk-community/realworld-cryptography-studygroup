#!/usr/bin/env python
# coding: utf-8
# License: MIT
# Author: Chris Ward <chris@zeroknowledge.fm>

__app_name__ = "rwc-exercise-01-01"
__version__ = "0.1.0"
'''
0.1.0: An example breaking MD5
'''

import hashlib
import os

from IPython.display import Image, display

DIGESTS = {
    'md5': hashlib.md5,
    'sha256': hashlib.sha256,
}


def _digest_bytes(str_bytes, lib):
    # str_bytes is expected to be encoded already
    _hash = lib()
    _hash.update(str_bytes)
    _digest = _hash.hexdigest()
    return _digest


def _digest(_input, lib):
    # Overwrite _input with file bytes if we have a valid path
    if os.path.exists(_input):
        with open(_input, "rb") as _file:
            str_bytes = _file.read()
    else:
        str_bytes = _input.encode('ascii')
    return _digest_bytes(str_bytes, lib)


def md5_digest(filepath):
    return _digest(filepath, hashlib.md5)


def sha2_digest(filepath, depth=256):
    return _digest(filepath, hashlib.sha256)


def detect_collision(m1, m2, hasher):
    _hasher = DIGESTS[hasher]  # eg... md5 => hashlib.md5
    d1 = _digest(m1, _hasher)
    d2 = _digest(m2, _hasher)
    collided = d1 == d2
    match_txt = '>>> Collision detected! <<<' if collided else ' OK '
    if collided:
        print(f'{match_txt} {hasher}:\n{d1}')
    else:
        print(f'{match_txt} {hasher}\n')
    return collided


def main():
    # Point to image files
    fn1 = 'assets/photo-1-md5hash-collide.jpeg'
    fn2 = 'assets/photo-2-md5hash-collide.jpeg'

    display(Image(filename=fn1))
    display(Image(filename=fn2))

    print("\nImage File Collision Detection")
    # Same messages, where m2 only one byte(?) diff: md5 returns same hash
    detect_collision(fn1, fn2, 'sha256')
    detect_collision(fn1, fn2, 'md5')

    print('-----')

    print("\nBinary File Collision Detection")
    # Point to binary files
    fn1 = 'assets/message1.bin'
    fn2 = 'assets/message2.bin'
    detect_collision(fn1, fn2, 'sha256')
    detect_collision(fn1, fn2, 'md5')


if __name__ == '__main__':
    main()
