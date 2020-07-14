capacity=2
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
            hold_curr = self.lookup.pop(key)
            # make new entry in hashtable
            self.lookup[key] = hold_curr
            # make changes in the doubly linked list
            # remove from the current position
            hold_curr_prev = hold_curr.prev
            hold_curr_next = hold_curr.next

            hold_curr_prev.next = hold_curr_next
            hold_curr_next.prev = hold_curr_prev

            # insert the removed node in the first position
            hold_nex = self.head.next
            self.head.next = hold_curr
            hold_curr.prev = self.head
            hold_curr.next = hold_nex
            hold_nex.prev = hold_curr
            return hold_curr.value
        elif key not in self.lookup:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node=self.lookup[key]
            val=node.value
            if (val==value):
                hold_curr= self.lookup.pop(key)
                # make new entry in hashtable
                self.lookup[key]=hold_curr
                # make changes in the doubly linked list
                #remove from the current position
                hold_curr_prev=hold_curr.prev
                hold_curr_next=hold_curr.next

                hold_curr_prev.next=hold_curr_next
                hold_curr_next.prev= hold_curr_prev

                #insert the removed node in the first position
                hold_nex=self.head.next
                self.head.next=hold_curr
                hold_curr.prev=self.head
                hold_curr.next=hold_nex
                hold_nex.prev=hold_curr

            elif (val!=value):
                # create new node
                newnode = DoubleList(value)
                # remove from hashtable (python dictionary) and from the doubly linked list
                hold_curr=self.lookup.pop(key)
                hold_curr_prev = hold_curr.prev
                hold_curr_next = hold_curr.next

                hold_curr_prev.next = hold_curr_next
                hold_curr_next.prev = hold_curr_prev

                # insert newnode at the index of the doubly linked list and in the hastable
                self.lookup[key] = newnode
                hold_nex = self.head.next
                self.head.next = newnode
                newnode.prev = self.head
                newnode.next = hold_nex
                hold_nex.prev = newnode

        elif key not in self.lookup:
            if len(self.lookup) != self.capacity:
                # create new node
                newnode = DoubleList(value)
                # insert key and newnode in the hashtable
                self.lookup[key] = newnode
                # insert node in the  doubly linkedlist
                hold_nex = self.head.next
                self.head.next = newnode
                newnode.prev = self.head
                newnode.next = hold_nex
                hold_nex.prev = newnode

            elif len(self.lookup) == self.capacity:
                # remove least recently used one (in dicionary node present at 0th index)
                remove_key=next(iter(self.lookup))
                remove_node=self.lookup.pop(remove_key) # hold node add but remove it from the hashtable

                #remove from doubly linkedlist
                hold_curr_prev = remove_node.prev
                hold_curr_next = remove_node.next
                hold_curr_prev.next = hold_curr_next
                hold_curr_next.prev = hold_curr_prev

                # create new node... make entry in the hashtable and in double link list
                # create new node
                newnode = DoubleList(value)
                # insert key and newnode in the hashtable
                self.lookup[key] = newnode
                # insert node in the  doubly linkedlist
                hold_nex = self.head.next
                self.head.next = newnode
                newnode.prev = self.head
                newnode.next = hold_nex
                hold_nex.prev = newnode

    def double_linkedlist(self):
        l1 = DoubleList(-1)
        l2 = DoubleList(-2)
        l1.next = l2
        l2.prev = l1
        return l1

cache = LRUCache(capacity)

cache.put(2, 1);
cache.put(2, 2);
a=cache.get(2);   #// returns 2
cache.put(1, 1);
cache.put(4, 1);  #// evicts key 2
b=cache.get(2);   #// returns -1 (not found)


print(a, b)