from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.store=OrderedDict()
        self.freq={}
        self.capacity= capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        elif key in self.store:
            #get the key in the front and increase the count
            #store the value
            value=self.store[key]
            #pop the key
            self.store.pop(key)
            #maintain order
            self.store[key] = value
            #increase frequency
            self.freq[key] = self.freq[key] + 1
            
            return value

    def put(self, key: int, value: int) -> None:
        if len(self.store) < self.capacity:
            if key not in self.store:
                self.store[key] = value
                self.freq[key] = 1
            elif key in self.store:
                self.freq[key] = self.freq[key] + 1

        elif len(self.store) == self.capacity:
            print()


cache =  LFUCache( 2 )

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))      # // returns 1
cache.put(3, 3)   #// evicts key 2
print(cache.get(2))      # // returns -1 (not found)
print(cache.get(3))    # // returns 3.
print(cache.put(4, 4))   # // evicts key 1.
print(cache.get(1))      # // returns -1 (not found)
print(cache.get(3))      # // returns 3
print(cache.get(4))      # // returns 4
