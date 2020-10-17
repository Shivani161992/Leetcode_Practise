from random import choice
class RandomizedSet:

    def __init__(self):
        self.arr=[] # for random operation it gives O(1) complexity
        self.set={} # for insert and delete operation it gives O(1) complexity
        #key is value
        #value is array index


    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.arr.append(val)
            self.set[val]= (len(self.arr)-1)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        elif val in self.set:
            #first remove the item from the set
            removed_item_index= self.set.pop(val)  # 0
            #get array last element
            last_element=self.arr[-1] # 2

            if removed_item_index != len(self.arr)-1:
                # update in the dictionary
                self.set[last_element] = removed_item_index
                # remove element from the array also in O(1) complexity
                # to make this happen shift the element first to the last position and then pop it to gain O(1) complexity
                temp = self.arr[removed_item_index]
                self.arr[removed_item_index]= self.arr[len(self.arr)-1] # or last_element
                self.arr[len(self.arr) - 1] = temp
            self.arr.pop()
            return True



        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

    def getRandom(self) -> int:
        return choice(self.arr)


# randomizedSet = RandomizedSet();
# randomizedSet.insert(1); # Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); # Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); # Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); # getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); # Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); # 2 was already in the set, so return false.
# randomizedSet.getRandom(); # Since 2 is the only number in the set, getRandom() will always return 2.

r = RandomizedSet();
r.remove(0) #false
r.remove(0) #false
r.insert(0)#True
r.getRandom()
r.remove(0) #true
r.insert(0) #true    getting false

