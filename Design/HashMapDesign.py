class MyHashMap:

    def __init__(self):
        self.arr=[None]*10000
        """
        Initialize your data structure here.
        """

    def put(self, key: int, value: int) -> None:
        self.arr[key]=value
        """
        value will always be non-negative.
        """

    def get(self, key: int) -> int:
        if self.arr[key]!=None:
            return self.arr[key]
        else:
            return -1

        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

    def remove(self, key: int) -> None:
        if self.arr[key]!=None:
            self.arr[key]=None
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

o=MyHashMap()
o.remove(2);
o.put(3,11);
o.put(4,13);

o.put(15,6);
o.put(6,15);

o.put(8,8);
o.put(11,0);

a=o.get(11);            # returns 1
o.put(1,10);
o.put(12,14);
