#В качестве приоритета элемента выступает его числовое значение
from typing import List
class MaxHeap:
    def __init__(self) -> None:
        self.q = []


    def push(self, val: int) -> None:
        self.q.append(val)
        self.q.sort()
        
        
    def pop(self) -> int:
        return self.q.pop()


    def heapify(self, iterable: List[int]) -> None:
        self.q = iterable.sort()
