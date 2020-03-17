class new_list(list):
    def __sub__(self,other):
        raz = len(self) - len(other)
        if raz >= 0:
            res = [self[i] - other[i] for i in range(len(other))]
            for i in range(len(other),len(self)):
                res.append(self[i])
        else:
            res = [self[i] - other[i] for i in range(len(self))] 
            for i in range(len(self),len(other)):
                res.append(-other[i])
        return new_list(res)
    
    def __add__(self,other):
        res = []
        raz = len(self) - len(other)
        if raz >= 0:
            big_list = self
            small_list = other
        else:
            small_list = self
            big_list = other
        res = [small_list[i] + big_list[i] for i in range(len(small_list))]
        for i in range(len(small_list),len(big_list)):
            res.append(big_list[i])
        return new_list(res)
    
    def __gt__(self, other):
        return sum(self) > sum(other)
    def __lt__(self, other):
        return sum(self) < sum(other)
    def __ge__(self, other):
        return sum(self) >= sum(other)
    def __le__(self, other):
        return sum(self) <= sum(other)
    def __eq__(self,other):
        return sum(self) == sum(other)
    def __ne__(self, other):
        return sum(self) != sum(other)
