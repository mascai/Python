# Пул потоков, concurrent.futures.Future

from concurrent.futures import ThreadPoolExecutor, as_completed

def f(a):
    return a * a

# .shutdown() in exit
with ThreadPoolExecutor(max_workers=3) as pool: # ограничили число потоков
    results = [pool.submit(f, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())

'''
$ python 1.py
0
1
4
9
'''
