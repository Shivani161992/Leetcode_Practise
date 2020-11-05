
#this is brute force method
#In this  method we are adding elements in a array
#now adding the element in a array is costly. space complexity is O(n) where n is the number of elements
#time complexity of adding a number is O(1) though
#time complexity of finding a median is O(nlogn) because we have to sort the elements also
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


#here we will be using the concept of two heaps
#it will keep track of finding the median
# what we need to do is keep balancing the min heap and max heap
#create a max heap and min heap. In max heap all elements will be less than median and in min heap all the elements will be greater than median

import heapq
class MedianFinder_heap:

    def __init__(self):
        self.max_lmedian=[]
        self.min_gmedian=[]



    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_lmedian, -num)
        get_max= heapq.heappop(self.max_lmedian)
        heapq.heappush(self.min_gmedian, -get_max)

        if len(self.max_lmedian) < len(self.min_gmedian):
            get_min = heapq.heappop(self.min_gmedian)
            heapq.heappush(self.max_lmedian, -get_min)

    def findMedian(self) -> float:
        if len(self.max_lmedian) != len(self.min_gmedian):
            get_max = self.max_lmedian[0]
            return -get_max
        elif len(self.max_lmedian) == len(self.min_gmedian):
            avg= (-self.max_lmedian[0] + self.min_gmedian[0]) /2
            return avg

obj=MedianFinder_heap()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())  #1.5
obj.addNum(3)
print(obj.findMedian()) # 2
