#!/usr/bin/env python3
import sys
from chall3 import unxor, score

# use frequency scoring to find most englishy result
def detect_xor(a):
  ret = ""
  for line in a:
    ret = unxor(line) if score(unxor(line)) > score(ret) else ret
  return ret

if __name__ == "__main__":
  d = [bytearray.fromhex(l.strip()) for l in open(sys.argv[1]).readlines()]
  print(detect_xor(d).decode())

