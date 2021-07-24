capacity=2
class Node:
    def __init__(self, x):
        self.val= x
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def createDoublyLL(self):
        head= Node(-1)
        tail= Node(-2)
        head.next=tail
        tail.prev=head
        return head


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.lru=dict()
        self.linkedList= DoublyLinkedList().createDoublyLL()

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        else:
            getNode= self.lru[key]
            self.delete(getNode)
            del self.lru[key]
            self.lru[key]=getNode
            self.insertInFront(getNode)
            return getNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            getNode=self.lru[key]
            self.delete(getNode)
            del self.lru[key]
            createNode= Node(value)
            self.lru[key] = createNode
            self.insertInFront(createNode)
        elif key not in self.lru:
            if len(self.lru) < self.capacity:
                createNode = Node(value)
                self.lru[key] = createNode
                self.insertInFront(createNode)
            elif len(self.lru) >= self.capacity:
                for k in self.lru:
                    removeNode= self.lru[k]
                    self.delete(removeNode)
                    del self.lru[k]
                    break
                createNode = Node(value)
                self.lru[key] = createNode
                self.insertInFront(createNode)

    def insertInFront(self, node):
        if node:
            holdHead= self.linkedList
            holdNext= holdHead.next
            holdHead.next= node
            node.prev= holdHead
            node.next= holdNext
            holdNext.prev= node
    def delete(self, node):
        if node:
            getNext=node.next
            getPrev= node.prev
            getPrev.next= getNext
            getNext.prev= getPrev

cache = LRUCache(capacity)
cache.put(2, 1);
cache.put(2, 2);
a=cache.get(2);   #// returns 2
cache.put(1, 1);
cache.put(4, 1);  #// evicts key 2
b=cache.get(2);   #// returns -1 (not found)


print(a, b)