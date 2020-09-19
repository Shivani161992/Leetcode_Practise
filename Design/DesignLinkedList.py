class ListNode:
    def __init__(self, x):
        self.val=x
        self.next=None


class MyLinkedList:

    def __init__(self):
        self.top= ListNode(-1)
        self.head = self.top.next
        self.listsize=-1

    def get(self, index: int) -> int:
        if index > self.listsize :
            return -1
        elif index <= self.listsize :
            count = 1
            hold_head = self.head
            while self.head:
                if count == index:
                    value= self.head.val
                    self.head= hold_head
                    return value
                else:
                    self.head= self.head.next
                    count= count + 1
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val)
        curr_node = self.head
        self.head = newnode
        newnode.next = curr_node
        self.top.next=newnode

        # node count
        self.listsize= self.listsize + 1

    def addAtTail(self, val: int) -> None:
        newnode= ListNode(val)
        prev=None
        hold_head=self.head
        while self.head is not None:
            prev=self.head
            self.head = self.head.next

        prev.next=newnode
        self.head=hold_head
        # node count
        self.listsize = self.listsize + 1
        """
        Append a node of value val to the last element of the linked list.
        """

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.listsize:
            self.addAtTail(val)
        elif index < self.listsize:
            count = 0
            self.listsize = self.listsize + 1
            hold_head = self.head
            #Create new Node
            newnode = ListNode(val)

            while self.head is not None:
                if count == index - 1:
                    nex=self.head.next
                    self.head.next=newnode
                    newnode.next=nex
                    break
                if count != index - 1:
                    self.head= self.head.next
                    count= count + 1
            self.head = hold_head

        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

    def deleteAtIndex(self, index: int) -> None:
        if index <= self.listsize:
            count = 0
            hold_head= self.head
            prev=None
            while self.head:
                if count != index:
                    prev=self.head
                    self.head=self.head.next
                    count = count + 1
                elif count == index:
                    prev.next = self.head.next
                    self.listsize= self.listsize - 1
                    break
            self.head = hold_head
        """
        Delete the index-th node in the linked list, if the index is valid.
        """


linkedList=MyLinkedList()
linkedList.addAtHead(1);
#linkedList.deleteAtIndex(0);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  #// linked list becomes 1->2->3
x=linkedList.get(1);            #// returns 2
linkedList.deleteAtIndex(0);  #// now the linked list is 1->3
y=linkedList.get(0);            #// returns 3
#
print(x, y)