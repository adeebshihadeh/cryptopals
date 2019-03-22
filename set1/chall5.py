#!/usr/bin/env python3
import sys
from binascii import hexlify

def xor(plain, key):
  ret = list()
  for i, c in enumerate(plain):
    ret.append(ord(c) ^ ord(key[i % len(key)]))
  return bytearray(ret)

if __name__ == "__main__":
  plain = open(sys.argv[1]).read()
  key = sys.argv[2]
  print(hexlify(xor(plain, key)))
  
