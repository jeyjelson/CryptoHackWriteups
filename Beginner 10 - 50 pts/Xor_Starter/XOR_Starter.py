#import xor from pwn 
from pwn import xor

#bytes of ASCII string for "label"
label = b"label"

#xor each byte of label with 13
result = xor(label, 13)

#decode result to a python string and then print it
print(result.decode())

