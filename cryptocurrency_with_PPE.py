import time
from hashlib import md5
from random import choice
import concurrent.futures


tic = time.perf_counter()


def f():
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()
    if h.endswith("00000"):
        print(s, h)
        toc = time.perf_counter()
        print(toc - tic)


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        while True:
            executor.submit(f)


if __name__ == '__main__':
    main()