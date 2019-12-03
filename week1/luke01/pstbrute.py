from Crypto.Hash import SHA1
from itertools import product
from time import sleep
import sys
import string

c1 = '*@!#%&()^~{}'
c2 = string.digits
c3 = string.ascii_uppercase
c4 = string.ascii_lowercase

target = "42f82ae6e57626768c5f525f03085decfdc5c6fe"

for t in product(c1, c2, c3, c4):
    if sum([ord(c) for c in t]) % 128 == 24:
        s = ''.join(sorted(t))
        
        h = SHA1.new()
        h.update(s.encode())
        print(s, h.hexdigest())
        
        if h.hexdigest() == target:
            print(f'\nFOUND PASSWORD: {s}\n')
            sys.exit(0)

        sleep(0.0005) # Bare for syns skyld