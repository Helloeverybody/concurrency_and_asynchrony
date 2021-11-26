import time
from hashlib import md5
from random import choice

tic = time.perf_counter()
while True:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()
    toc = time.perf_counter()
    print(toc - tic)
    if h.endswith("00000"):
        print(s, h)
