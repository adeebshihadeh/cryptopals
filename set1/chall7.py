#!/usr/bin/env python3
import sys
from base64 import b64decode
from Crypto.Cipher import AES

def aes128_decrypt(cipher, key):
  c = AES.new(key, AES.MODE_ECB)
  return c.decrypt(cipher)

if __name__ == "__main__":
  cipher = b64decode(open(sys.argv[1]).read())
  key = ' '.join(sys.argv[2:])
  print(aes128_decrypt(cipher, key))


