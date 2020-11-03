class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode(1)
l12=ListNode(2)
l13=ListNode(3)
l14=ListNode(4)
l15=ListNode(5)
head.next=l12
l12.next=l13
l13.next=l14
l14.next=l15

k=2

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        elements=[]
        while head:
            elements.append(head.val)
            head=head.next

        hold=ListNode(-1)
        hold_head= hold
        k = k % len(elements)
        elements= elements[len(elements) - k:] + elements[:len(elements)-k]
        for i in elements:
            newnode=ListNode(i)
            hold.next= newnode
            hold= hold.next
        return hold_head.next



obj=Solution()
obj.rotateRight(head, k)