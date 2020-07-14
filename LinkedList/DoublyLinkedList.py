capacity=4
class DoubleList:
    def __init__(self, x):
        self.value=x
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head= self.double_linkedlist()
        self.lookup={}

    def get(self, key: int) -> int:
        if key in self.lookup:
            val =self.lookup[key]
            return val.value
        elif key not in self.lookup:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lookup) != self.capacity:
            newnode=DoubleList(value)
            self.lookup[key]=newnode
            first=0
            while self.head:
                first = first + 1
                if first==1:
                    hold_next= self.head.next
                    self.head.next=newnode
                    newnode.prev=self.head
                    newnode.next= hold_next
                    hold_next.prev=newnode
                    break
        elif len(self.lookup) != self.capacity:
            if key not in self.lookup:
                newnode = DoubleList(value)
                self.lookup[key] = newnode
                first = 0
                while self.head:
                    first = first + 1
                    if first == 1:
                        hold_next = self.head.next
                        self.head.next = newnode
                        newnode.prev = self.head
                        newnode.next = hold_next
                        hold_next.prev = newnode
                        break

    #
    def double_linkedlist(self):
        l1 = DoubleList(-1)
        l2 = DoubleList(-2)
        l1.next = l2
        l2.prev = l1
        return l1

cache = LRUCache(capacity)

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       #// returns 1
cache.put(3, 3);    #// evicts key 2
cache.get(2);       #// returns -1 (not found)
cache.put(4, 4);    #// evicts key 1
cache.get(1);       #// returns -1 (not found)
cache.get(3);       #// returns 3
cache.get(4);       #// returns 4