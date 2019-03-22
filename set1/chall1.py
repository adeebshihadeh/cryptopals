#!/usr/bin/env python3
import sys
from base64 import b64encode 

if __name__ == "__main__":
  data = bytearray.fromhex(sys.argv[1])
  print(b64encode(data))

