class MyHashSet:

    def __init__(self):
        self.arr=[None]*1000000
        self.count=0

    def add(self, key: int) -> None:
        if key not in self.arr:
            self.arr[self.count]=key
            self.count = self.count + 1

    def remove(self, key: int) -> None:
        if key in self.arr:
            self.count = self.count - 1
            self.arr.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.arr:
            return True
        else:
            return False

hashSet=MyHashSet()
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);  #  // returns true
hashSet.contains(3);   # // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    #// returns true
hashSet.remove(2);
hashSet.contains(2);    #// returns false (already removed)