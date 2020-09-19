class MedianFinder:

    def __init__(self):
        self.arry=[]
        self.median=-1
        self.type='even'

    def addNum(self, num: int) -> None:
        if self.type=='even':
            self.type='odd'
            self.median = self.median + 1
        elif self.type=='odd':
            self.type='even'
        self.arry.append(num)
        self.arry.sort()


    def findMedian(self) -> float:
        if self.type=='odd':
            return self.arry[self.median]
        elif self.type=='even':
            sum = self.arry[self.median]
            sum= (sum + self.arry[self.median+1])/2
            return sum




obj=MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())  #1.5
obj.addNum(3)
print(obj.findMedian()) # 2
