class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)

l1.next=l2
l2.next=l3
l3.next=l4

l2_1= ListNode(5)
l2_2= ListNode(6)
l2_3= ListNode(7)

l2_1.next= l2_2
l2_2.next= l2_3
l2_3.next= l3

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        holdA= headA
        holdB= headB

        while headA is not headB:
            if headA is not None:
                headA=headA.next
            else:
                headA=holdB

            if headB is not None:
                headB=headB.next
            else:
                headB=holdA

        return headA




o=Solution()
y=o.getIntersectionNode(l1, l2_1)
print(y)