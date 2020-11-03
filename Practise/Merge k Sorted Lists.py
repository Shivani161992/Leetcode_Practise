# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l11=ListNode(1)
l12=ListNode(4)
l13=ListNode(5)
l11.next=l12
l12.next=l13

l21=ListNode(1)
l22=ListNode(3)
l23=ListNode(4)
l21.next=l22
l22.next=l23

l31=ListNode(2)
l32=ListNode(6)
l31.next=l32

lists=[l11, l21, l31]

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h= [(v.val, idx) for idx, v in enumerate(lists) if v]
        heapq.heapify(h)
        # pop the minimum element
        # define head for the linked list
        head= ListNode(-1)
        hold_head= head

        while len(h) !=0:
            #pop the smallest element from heap
            get_smallest= heapq.heappop(h)
            newnode=ListNode(get_smallest[0])

            # generate new node with the value and append it in the head
            head.next=newnode
            head=head.next

            # update list, get the tuple and push it in the heap
            get_ll= lists[get_smallest[1]]
            if get_ll.next:
                lists[get_smallest[1]]= lists[get_smallest[1]].next
                get_ll= get_ll.next
                insert= (get_ll.val, get_smallest[1])
                heapq.heappush(h, insert)

        return hold_head.next

obj=Solution()
print(obj.mergeKLists(lists))