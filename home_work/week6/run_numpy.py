import numpy as np



def foo(l):
    res = tuple()
    for i in range(len(l)):
        a=l[i]
        l[i]=1
        print(l)
        res.append(l)
        print(res)
        l[i]=a


    return list(np.prod(res,axis=1))


print(foo([1,2,3]))
