class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head=ListNode(1)
l2=ListNode(2)
# l3=ListNode(3)
# l4=ListNode(4)
# l5=ListNode(5)

head.next=l2
# l2.next=l3
# l3.next=l4
# l4.next=l5

k=2

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k ==1:
            return head
        else:
            main_head=None #this will be the main head to return if k is smaller than the length of the linked list
            hold_head=None
            hold_next=None
            hold_prev=None
            count=0
            #store head to return if k is greater than the length of the linked list
            hhead=head
            while head is not None:
                #increase the count
                count = count + 1
                #check whether the count is equal to k or not
                if count < k:
                    # if count is 1 then store it to make the link easier
                    if count == 1:
                        hold_head= head
                    head=head.next
                elif count == k:
                    #hold next
                    hold_next=head.next
                    #break the link of next nodes
                    head.next=None
                    #get reserve of the string
                    get_reverse= self.reverse(hold_head)
                    if main_head is None:
                        #if main head is empty then assign value else attach the link
                        main_head=get_reverse
                    elif main_head is not None:
                        hold_prev.next=get_reverse


                    hold_prev = hold_head
                    head= hold_next
                    count = 0
            if main_head is None:
                return hhead
            # consider the case when the length of the linked list is same as k
            elif main_head is not None and hold_prev != hold_head:
                hold_prev.next=hold_head
            return main_head




    #reverse linked list
    def reverse(self, head):
        prev=None
        nex= None
        while head:
            nex=head.next
            head.next=prev
            prev=head
            head=nex
        return prev



obj=Solution()
print(obj.reverseKGroup(head, k))