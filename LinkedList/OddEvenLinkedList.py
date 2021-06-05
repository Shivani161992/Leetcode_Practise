# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)

head.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        else:
            holdOdd=head
            oddList=None
            evenList=None
            holdEven=None
            type='odd'
            while head:
                if type=='odd':
                    type='even'
                    if oddList==None:
                        oddList=head
                    else:
                        oddList.next=head
                        oddList=oddList.next
                elif type=='even':
                    type = 'odd'
                    if evenList==None:
                        evenList=head
                        holdEven=evenList
                    else:
                        evenList.next = head
                        evenList = evenList.next
                head= head.next
            if evenList !=None:
                evenList.next=None
            oddList.next=holdEven

        return holdOdd


obj=Solution()
print(obj.oddEvenList(head))
