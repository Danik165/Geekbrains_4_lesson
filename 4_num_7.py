from itertools import count
from math import factorial


def gen():
    for el in count(1):
        yield factorial(el)


gen = gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
