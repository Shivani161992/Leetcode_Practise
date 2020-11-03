from typing import List
from collections import Counter
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique={}
        self.all=set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if len(self.unique)!=0:
            return list(self.unique.keys())[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value not in self.all:
            self.all.add(value)
            self.unique[value]=None
        elif value in self.all and value in self.unique :
            del self.unique[value]



firstUnique = FirstUnique([2,3,5, 5]);
print(firstUnique.showFirstUnique())#; // return 2
firstUnique.add(5)#;            // the queue is now [2,3,5,5]
print(firstUnique.showFirstUnique())#; // return 2
firstUnique.add(2)#;            // the queue is now [2,3,5,5,2]
print(firstUnique.showFirstUnique())#; // return 3
firstUnique.add(3)#;            // the queue is now [2,3,5,5,2,3]
print(firstUnique.showFirstUnique())#; // return -1
