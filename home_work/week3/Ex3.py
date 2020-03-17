class MedianFinder:
    def __init__(self):
        self.list = []
        
        
    def addNum(self, num: int) -> None:
        self.list.append(num)
        
        
    def findMedian(self) -> float:
        self.list = sorted(self.list)
        if len(self.list) % 2 != 0:
            return float(self.list[len(self.list) // 2])
        else:
            return (self.list[len(self.list) // 2 - 1] +  self.list[(len(self.list) // 2)]) / 2
