#!/usr/bin/env python3
import sys

# how englishy is a string?
# should non-letters have score of zero?
def score(a):
  f = "zqjxkvbywgpfmucdlhrsnioate"
  return sum([f.index(chr(c).lower()) if chr(c) in f else 0 for c in a])

# use score() to return most englishy result
def unxor(a):
  ret, key = list(), ""
  for k in range(0, 255):
    b = [k ^ c for c in a]
    if score(b) > score(ret): ret, key = b, k
  return bytearray(ret), key 

if __name__ == "__main__":
  arg = bytearray.fromhex(sys.argv[1])
  print(unxor(arg)[0].decode())

