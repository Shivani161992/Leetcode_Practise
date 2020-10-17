class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode(5)
l12=ListNode(2)
l13=ListNode(4)
l14=ListNode(3)
head.next=l12
l12.next=l13
l13.next=l14
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        else:
            prev = None
            next_ptr = None
            while head:
                next_ptr = head.next
                head.next = prev
                prev = head
                head = next_ptr
            return prev

obj=Solution()
obj.reverseList(head)
