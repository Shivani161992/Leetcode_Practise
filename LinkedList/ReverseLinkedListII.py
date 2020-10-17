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
m=1
n=4

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count=0
        hold_head=head
        hold_start=None
        hold_reverse_end=None
        prev=None
        next_ptr=None
        while head:
            count = count+1
            if count < m:
                hold_start=head
                head= head.next
            elif count >=m and count <= n:
                if count == m:
                    hold_reverse_end=head

                next_ptr=head.next
                head.next =prev
                prev=head
                head=next_ptr
            if count >= n:
                if hold_start:
                    hold_start.next=prev
                elif head is None :
                    return prev
                elif hold_start is None:
                    hold_reverse_end.next=head
                    return prev

                hold_reverse_end.next=head
                break
        return hold_head




obj=Solution()
obj.reverseBetween(head, m, n)


