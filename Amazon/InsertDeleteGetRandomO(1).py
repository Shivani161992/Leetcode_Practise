import random
class RandomizedSet:

    def __init__(self):
        self.arr=[]
        self.dic={}


    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.arr.append(val)
            self.dic[val]= len(self.arr)-1
            return True
        elif val in self.dic:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            getIdx= self.dic[val]  # 1
            #get arr last element
            getLas =self.arr[len(self.arr)-1] # 4

            #replace in arr
            self.arr[len(self.arr) - 1]= val
            self.arr[getIdx]= getLas
            self.arr.pop()

            #Update dictionary
            self.dic[getLas]= getIdx
            del self.dic[val]
            return True
        elif val not in self.dic:
            return False

    def getRandom(self) -> int:
            return random.choice(self.arr)


randomizedSet =  RandomizedSet();
print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1)) # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2)) # 2 was already in the set, so return false.
print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.
