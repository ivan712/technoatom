import numpy as np
import random
import cProfile
from memory_profiler import profile
import logging

logging.basicConfig(filename = 'my_log.log', level =logging.DEBUG)




def block(a,i):
    mult = 1
    logging.debug("---------------------")
    logging.debug(f"start block a for element {i}")
    logging.debug(f"a ={a}")
    for j in a:
        mult*=j
    logging.debug(f"mult ={mult}")
    logging.debug("stop block a")
    logging.debug("----------------------")
    return mult


def foo(l):
    res = []
    logging.debug("---------------------")
    logging.debug(f"start foo({l})")
    for i in l:
        a = l.copy()
        a.remove(i)


        res.append(block(a,i))
    logging.debug(f"res = {res}")
    logging.debug("Stop foo")
    logging.debug("-----------------------")
    return res

l=[random.randint(3,10) for _ in range(3)]
foo(l)

#cProfile.run('foo(l)')
