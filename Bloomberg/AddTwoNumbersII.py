class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



l1=ListNode(5)
l12=ListNode(2)
l13=ListNode(4)
l14=ListNode(3)
l1.next=l12
l12.next=l13
l13.next=l14

l2=ListNode(5)
l22=ListNode(6)
l23=ListNode(4)
l2.next=l22
l22.next=l23

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1=[]
        list2=[]
        carry=0
        head=ListNode(-1)
        hold_head=head
        while l1:
            list1.append(l1.val)
            l1=l1.next
        while l2:
            list2.append(l2.val)
            l2=l2.next

        while list1 or list2:
            val1= list1.pop() if list1 else 0
            val2= list2.pop() if list2 else 0
            sum = val1 + val2 + carry

            carry, node=divmod(sum, 10)

            newnode=ListNode(node)
            #add node in the begning
            hold_nex=head.next
            head.next=newnode
            newnode.next=hold_nex

        if carry !=0:
           newnode=ListNode(carry)
           #add node in the begni
           hold_nex=head.next    
           head.next=newnode   
           newnode.next=hold_nex
        return hold_head.next




obj=Solution()
obj.addTwoNumbers(l1, l2)