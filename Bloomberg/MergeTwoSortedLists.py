class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



l1=ListNode(1)
l12=ListNode(2)
l13=ListNode(4)
l14=ListNode(7)
l1.next=l12
l12.next=l13
l13.next=l14

l2=ListNode(1)
l22=ListNode(3)
l23=ListNode(4)
l2.next=l22
l22.next=l23

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(-1)
        hold_head=head
        while l1 or l2:
            if l1.val <= l2.val:
                head.next=l1
                head= head.next
                l1=l1.next
            elif l2.val < l1.val:
                head.next = l2
                head = head.next
                l2 = l2.next

        if l1 is None:
            head.next=l2
        elif l2 is None:
            head.next=l1
        return hold_head.next

Obj=Solution()
Obj.mergeTwoLists(l1, l2)