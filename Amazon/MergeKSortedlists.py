
from typing import List
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:
            return []
        else:
            head= ListNode('#')
            holdHead=head
            hold=[]
            for idx, node in enumerate(lists):
                hold.append([node.val, idx])
            heapq.heapify(hold)
            #get Node
            getNode=heapq.heappop(hold)
            getidx= getNode[1]
            #get
            head.next= lists[getidx]
            head= head.next



            print('jds')

            return holdHead.next



obj=Solution()
print(obj.mergeKLists(lists))