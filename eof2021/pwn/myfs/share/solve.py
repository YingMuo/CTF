#!/usr/bin/env python3
import hashlib
import sys

def is_valid(digest, difficulty, zeros):
    if sys.version_info.major == 2:
        digest = [ord(i) for i in digest]
    bits = ''.join(bin(i)[2:].zfill(8) for i in digest)
    return bits[:difficulty] == zeros


def solve(h, len):
    prefix = h
    difficulty = len
    zeros = '0' * difficulty
    i = 0
    while True:
        i += 1
        s = prefix + str(i)
        if is_valid(hashlib.sha256(s.encode()).digest(), difficulty, zeros):
            return i
            