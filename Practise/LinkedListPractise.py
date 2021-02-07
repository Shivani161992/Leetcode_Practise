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
class Solution: 
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        else:
            prev = None
            nex = None
            while head:
                nex = head.next
                head.next=prev
                prev= head
                head= nex
            return prev 
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        else:
            slow= head
            fast= head
            while fast and fast.next:
                slow= slow.next
                fast= fast.next.next
            return slow.val
        

obj= Solution()
print(obj.middleNode(head))

        