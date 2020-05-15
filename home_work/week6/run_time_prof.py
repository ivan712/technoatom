import cProfile, pstats, io
from pstats import SortKey
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



pr = cProfile.Profile()
pr.enable()


l=[random.randint(3,10) for _ in range(10000)]
foo(l)



pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
