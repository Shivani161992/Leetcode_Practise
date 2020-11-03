from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.store=OrderedDict()
        self.freq=OrderedDict()
        self.capacity= capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        elif key in self.store:
            #get the key in the front and increase the count
            #store the value
            # value=self.store[key]
            # #pop the key
            # self.store.pop(key)
            # #maintain order
            # self.store[key] = value
            #increase frequency
            #delete the key from the frequency and add it again
            freq = self.freq[key]
            self.freq.pop(key)
            self.freq[key] = freq + 1
            return self.store[key]

    def put(self, key: int, value: int) -> None:
        if len(self.store) < self.capacity:
            if key not in self.store:
                self.store[key] = value
                self.freq[key] = 1
            elif key in self.store:
                # self.store.pop(key)
                # # maintain order
                self.store[key] = value
                # increase frequency
                # delete the key from the frequency and add it again
                freq = self.freq[key]
                self.freq.pop(key)
                self.freq[key] = freq + 1

        elif len(self.store) == self.capacity:
            if key not in self.store:
                #get all the elements from a dictionary and sort them according to the frequency
                get_elements = list(self.freq.items())
                get_elements.sort(key=lambda x: x[1])
                if get_elements != []:
                    popkey=get_elements[0][0]
                    self.store.pop(popkey)
                    self.freq.pop(popkey)
                    #put element in the hash map
                    self.store[key] = value
                    self.freq[key] = 1
            elif key in self.store:
                # self.store.pop(key)
                # # maintain order
                self.store[key] = value
                # increase frequency
                # delete the key from the frequency and add it again
                freq = self.freq[key]
                self.freq.pop(key)
                self.freq[key] = freq + 1





cache =  LFUCache(0)
cache.put(0, 0)
print(cache.get(0))

# cache.put(2, 2)
# print(cache.get(1))      # // returns 1
# cache.put(3, 3)   #// evicts key 2
# print(cache.get(2))      # // returns -1 (not found)
# print(cache.get(3))    # // returns 3.
# cache.put(4, 4)  # // evicts key 1.
# print(cache.get(1))      # // returns -1 (not found)
# print(cache.get(3))      # // returns 3
# print(cache.get(4))      # // returns 4
