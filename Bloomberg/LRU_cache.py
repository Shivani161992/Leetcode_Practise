class Node:
    def __init__(self, x):
        self.value=x
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.key={}
        self.value= self.doubly_linkedlist()

    def doubly_linkedlist(self):
        head=Node(-1)
        tail=Node(-2)
        head.next=tail
        tail.prev=head
        return head

    def get(self, key: int) -> int:
        if key not in self.key:
            return -1
        elif key in self.key:
            get= self.key.pop(key)
            self.key[key] = get
            #move the node in the front
            self.move_node(get)
            return get.value

    def move_node(self, node):
        #first delete the node
        node.prev.next=node.next
        node.next.prev=node.prev

        #insert the node in the begning
        self.insert_node(node)

    def insert_node(self, newnode):
        hold_next = self.value.next
        self.value.next = newnode
        newnode.prev = self.value

        newnode.next = hold_next
        hold_next.prev = newnode
    def remove_node(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def put(self, key: int, value: int) -> None:
        if key not in self.key:
            #evict the node if capacity reached
            if len(self.key) == self.capacity:
                #get the index of the oldest element
                get_items= list(self.key.items())
                #extract key
                last_key=get_items[0][0]
                #pop the key
                old_node=self.key.pop(last_key)
                #delete the node
                self.remove_node(old_node)
            # create new node
            newnode = Node(value)
            # insert it in the hashmap
            self.key[key] = newnode
            # insert the node in the doubly linked list
            self.insert_node(newnode)

        elif key in self.key:
            get = self.key.pop(key)
            self.key[key] = get
            get.value=value
            # mode the node in the front
            self.move_node(get)
            return get.val





cache = LRUCache(2)
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)
cache.get(3);       # returns 3
cache.get(4);       # returns 4
