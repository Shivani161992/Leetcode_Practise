
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None

l1=Node(1)
l2=Node(2)
l3=Node(3)
l4=Node(4)
l5=Node(5)
l6=Node(6)

l7=Node(7)
l8=Node(8)
l9=Node(9)
l10=Node(10)
l11=Node(11)
l12=Node(12)
l13=Node(13)

l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=l6
#child
l3.child=l7
l7.next=l8
l8.next=l9
l9.next=l10

#child
l8.child=l11
l11.next=l12

#child
l12.child=l13

l2.prev=l1
l3.prev=l2
l4.prev=l3
l5.prev=l4
l6.prev=l5
l8.prev=l7
l9.prev=l8
l10.prev=l9
l12.prev = l11






class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        hold_head=head
        next_pointer=[]
        while head:
            if head.child is None:
                if head.next is None and len(next_pointer) != 0:
                    nxt= next_pointer[len(next_pointer)-1]
                    head.next=nxt
                    nxt.prev=head
                    next_pointer.pop()
                head=head.next
            elif head.child is not None:
                if head.next is not None:
                    next_pointer.append(head.next)
                head.next=head.child
                head.child.prev=head
                head.child=None
                if head.next is None and len(next_pointer) != 0:
                    nxt = next_pointer[:-1]
                    head.next = nxt
                    nxt.prev = head
                    next_pointer.pop()
                head = head.next

        head=hold_head


obj=Solution()
obj.flatten(l1)