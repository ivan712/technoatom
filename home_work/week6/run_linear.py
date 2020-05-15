def foo(l):
    if len(l)==1:
        return l
    l1 = []
    l2 = []
    mul_l1 = 1
    mul_l2 = 1
    length = len(l)
    for i in range(length-1):
        mul_l1*=l[i]
        mul_l2*=l[length-i-1]
        l1.append(mul_l1)
        l2.append(mul_l2)
    res = [l2.pop()]

    l2.reverse()

    for i in range(length-2):
            res.append(l1[i]*l2[i])
    res.append(l1.pop())
    return res

l = [1,2,3]
print(foo(l))
