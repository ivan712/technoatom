import numpy as np
import random
import cProfile
from memory_profiler import profile



def block(a):
    mult = 1

    for j in a:
        mult*=j
    return mult

@profile
def foo(l):
    res = []
    for i in l:
        a = l.copy()
        a.remove(i)
        res.append(block(a))
    return res

l=[random.randint(3,10) for _ in range(3)]
foo(l)

#cProfile.run('foo(l)')
