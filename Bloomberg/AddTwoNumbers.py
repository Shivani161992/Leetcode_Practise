class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



l1=ListNode(2)
l12=ListNode(4)
l13=ListNode(3)
l1.next=l12
l12.next=l13

l2=ListNode(5)
l22=ListNode(6)
l23=ListNode(4)
l2.next=l22
l22.next=l23
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        hold_head = head
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            carry, node = divmod(sum, 10)

            newnode = ListNode(node)
            head.next = newnode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            head = head.next

        if carry != 0:
            newnode = ListNode(carry)
            head.next = newnode

        return hold_head.next


obj=Solution()
obj.addTwoNumbers(l1, l2)
