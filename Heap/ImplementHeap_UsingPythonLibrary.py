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
li = [5, 7, 9, 1, 3]
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merged = None
        hold = None
        h=[(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        while len(h) != 0:
            pop=heapq.heappop(h)
            if merged==None:
                merged = lists[pop[1]]
                hold = merged
            elif merged!=None:
                merged.next = lists[pop[1]]
                merged = merged.next
            if lists[pop[1]].next:
                lists[pop[1]] = lists[pop[1]].next
                heapq.heappush(h, (lists[pop[1]].val, pop[1]))
            else:
                lists[pop[1]] = None
        return hold

obj=Solution()
print(obj.mergeKLists(lists))