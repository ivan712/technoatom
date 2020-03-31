from typing import List
class MaxHeap:
    def __init__(self) -> None:
        self.q = []

        
    def push(self, val: int) -> None:
        self.q.append(val)
        i = len(self.q)-1
        parent = (i-1) // 2
        while (parent >= 0 and self.q[parent] < self.q[i]):
            tmp = self.q[parent]
            self.q[parent] = self.q[i]
            self.q[i] = tmp
            i = parent
            parent = (i-1) //2

            
    def pop(self) -> int:
        res = self.q[0]
        self.q[0] = self.q.pop()
        i = 0
        while True:
            left = 2*i+1
            right = 2*i+2
            parent = i
            if (left < len(self.q) and self.q[parent] < self.q[left]):
                parent = left
            if (right < len(self.q) and self.q[parent] < self.q[right]):
                parent = right
            if (parent == i):
                break
            tmp = self.q[i]
            self.q[i] = self.q[parent]
            self.q[parent] = tmp
            i = parent
        print(self.q)
        return res

    
    def heapify(self, iterable: List[int]) -> None:
        self.q = []
        for i in iterable:
            self.push(i)
                
