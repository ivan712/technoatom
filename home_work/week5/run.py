import example
class CMatrix:
    def __init__(self,l):
        self.l = l

    def __mul__(self,a):
        if (type(a) == int):
            return CMatrix(example.mult_koef(self.l,a))
        return CMatrix(example.mult_mat(self.l,a.l))

    
    def mult_koef(self,koef):
        return CMatrix(example.mult_koef(self.l,koef))

 
    def div_koef(self,koef):
        return CMatrix(example.div_koef(self.l,koef))
    
    def get_el(self,el):
        return example.get_el(self.l,el)

    def in_matrix(self,el):
        return example.in_matrix(self.l,el)

    def __add__(self,a):
        return CMatrix(example.sum_mat(self.l,a.l))
    
    def tranc(self):
        return CMatrix(example.tranc_mat(self.l))
    
    def __str__(self):
        a = "Matrix:\n"
        for i in self.l:
            a += str(i)+"\n"
        return a
    
    def __repr__(self):
        return "Matrix: " + str(self.l)


class Matrix:
    def __init__(self,l):
        self.l = l
    def __mul__(self,b):
        el = 0
        res = []
        row = []
        for i in range(len(self.l)):
            for j in range(len(b.l[0])):
                for k in range(len(b.l)):
                    el += self.l[i][k]*b.l[k][j]
                row.append(el)
                el = 0
            res.append(row)
            row = []
        return Matrix(res)
    




if __name__=="__main__":
    m1=CMatrix([[1,2,3]])
    m2=CMatrix([[1,2]])
    print str(m1.l)+" * "+str(m2.l)+ " = "
    res = m1*m2


    
    print str(m1.l)+" + "+str(m2.l)+" = "
    res=m1+m2

    m1 = CMatrix([[1,2]])
    m2 = CMatrix([[2],[4]])
    res = m1*m2
    print str(m1.l)+" * "+str(m2.l)+" = "+str(res.l)


    m1 = CMatrix([[1,2],[3,4]])
    m2 = CMatrix([[5,6],[7,8]])
    res = m1*m2
    print str(m1.l)+" * "+str(m2.l)+" = "+str(res.l)

    res = m1*3
    print str(m1.l)+" * "+str(3)+" ="+ str(res.l)

    res = m2.div_koef(2)
    print str(m2.l) + " / "+str(2)+" = "+str(res.l)

    a = tuple([1,1])
    res = m1.get_el((1,1))
    print str(m1.l)+"  " +"get_el((1,1)) = "+str(res)

    res = m1.in_matrix(2)
    print str(m1.l)+"  "+"in_matrix(2) is "+str(res)

    res = m1+m2
    print str(m1.l)+" + "+str(m2.l)+" = "+str(res.l)

    res = m1.tranc()
    print str(m1.l)+" trancposition "+str(res.l)
