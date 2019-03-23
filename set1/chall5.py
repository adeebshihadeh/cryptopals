#!/usr/bin/env python3
import sys
from binascii import hexlify

def xor(a, key):
  ret = list()
  for i, c in enumerate(a):
    ret.append(c ^ key[i % len(key)])
  return bytearray(ret)

if __name__ == "__main__":
  plain = bytearray([ord(c) for c in open(sys.argv[1]).read()])
  key = bytearray([ord(c) for c in sys.argv[2]])
  print(hexlify(xor(plain, key)))


