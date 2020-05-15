from run import *
import random
import time
dim = 300
l1 = [[random.randint(0,1000) for _ in range(0,dim)] for _ in range(0,dim)]
l2 = [[random.randint(0,1000) for _ in range(0,dim)] for _ in range(0,dim)]

m1 = Matrix(l1)
m2 = Matrix(l2)

Cm1 = CMatrix(l1)
Cm2 = CMatrix(l2)

t1 = time.time()
res = m1*m2
t2 = time.time()
t = t2-t1
print "Python time: " + str(t)

t1 = time.time()
Cres = Cm1*Cm2
t2 = time.time()
t = t2 - t1
print "C time: " + str(t) 

print "equal?" + str(res.l == Cres.l)
