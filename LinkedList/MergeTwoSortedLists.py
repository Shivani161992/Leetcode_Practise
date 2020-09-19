# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l11=ListNode(1)
l12=ListNode(2)
l13=ListNode(4)
l11.next=l12
l12.next=l13

l21=ListNode(1)
l22=ListNode(3)
l23=ListNode(4)
l21.next=l22
l22.next=l23
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            head=ListNode(-1)
            hold=head
            while l1 and l2:
                if l1.val <= l2.val:
                    head.next=l1
                    l1=l1.next
                elif l1.val > l2.val:
                    head.next=l2
                    l2=l2.next
                head = head.next


            head.next=l2 if l1 is None else l1

            return hold.next




obj=Solution()
print(obj.mergeTwoLists(l11, l21))