#!/usr/bin/env python3
import sys
from base64 import b64decode
from itertools import permutations
from chall3 import unxor 
from chall5 import xor

# get hamming distance 
def hamming(a, b):
  ret = 0
  for i, j in zip(a, b):
    ret += sum(int(n) for n in bin(i^j)[2:])
  return ret + abs(len(a)-len(b))

# break repeating key xor
def xor_smash(a):
  ks, dmin =  None, None
  for s in range(2, 50):
    b = list(permutations([a[n*s:n*s+s] for n in range(4)], 2))
    d = sum([hamming(i, j) for i, j in b]) / (len(b)*s) 
    if ks is None or d < dmin: ks, dmin = s, d
  
  blocks = [list() for _ in range(ks)]
  for b in [a[i:i+ks] for i in range(0, len(a), ks)]:
    for j, bb in enumerate(b):
      blocks[j].append(bb)

  key = [unxor(c)[1] for c in blocks]
  return xor(a, key), key

if __name__ == "__main__":
  enc = b64decode(open(sys.argv[1]).read())
  print(xor_smash(enc)[0].decode())


