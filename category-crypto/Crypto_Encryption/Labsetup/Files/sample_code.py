#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

MSG   = "A message"
HEX_1 = "aabbccddeeff1122334455"
HEX_2 = "1122334455778800aabbdd"

# Convert ascii string to bytearray
D1 = bytearray(MSG, 'utf-8')

# Convert hex string to bytearray
D2 = bytearray.fromhex(HEX_1)
D3 = bytearray.fromhex(HEX_2)

r1 = xor(D1, D2)
r2 = xor(D2, D3)
r3 = xor(D2, D2)

# Convert bytearray to hex and print
print(r1.hex())
print(r2.hex())
print(r3.hex())

# Convert bytearray to text and print
print(D1.decode('utf-8'))

# Apply PKCS5 padding to a message prior to encryption
# for Task 6.3.
msg = "A message"
padding = 16 - (len(msg) % 16)
MSG = bytearray(msg, 'utf-8')
MSG.extend([padding] * padding)
