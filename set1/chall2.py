#!/usr/bin/env python3
import sys

def xor(a, b):
  ret = list()
  for ab, bb in zip(a, b):
    ret.append(ab^bb)
  return bytearray(ret) 

if __name__ == "__main__":
  a, b = sys.argv[1:3]
  a, b = bytearray.fromhex(a), bytearray.fromhex(b)
  print(xor(a, b).hex())

