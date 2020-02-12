"""
?: boolean
h: short
l: long
i: int
f: float
q: long long int
полный список: https://docs.python.org/3/library/struct.html#format-characters
"""

import struct

v1 = struct.pack('hhl', 5, 10, 15)
print(v1)
print(struct.unpack('hhl', v1))

v2 = struct.pack('iii', 10, 20, 30)
print(v2)
print(struct.unpack('iii', v2))
