import numpy as np
import random


def block(a):
    mult = 1
    for j in a:
        mult*=j
    return mult


def foo(l):
    res = []
    for i in l:
        a = l.copy()
        a.remove(i)
        res.append(block(a))
    return res

l=[random.randint(3,10) for _ in range(3)]
l1 = [2,3,2,2]
print(foo(l1))
#l1 = [2,3,2]
