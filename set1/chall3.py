#!/usr/bin/env python3
import sys

# how englishy is a string?
# http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
# added space as most frequent
def score(a):
  f = {" ": 15, "e": 12.02, "t": 9.10, "a": 8.12, "o": 7.68, "i": 7.31, "n": 6.95, "s": 6.28, "r": 6.02, "h": 5.92, "d": 4.32, "l": 3.98, "u": 2.88, "c": 2.71, "m": 2.61, "f": 2.30, "y": 2.11, "w": 2.09, "g": 2.03, "p": 1.82, "b": 1.49, "v": 1.11, "k": 0.69, "x": 0.17, "q": 0.11, "j": 0.10, "z": 0.07}
  return sum([f.get(chr(c).lower(), 0) for c in a])

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

