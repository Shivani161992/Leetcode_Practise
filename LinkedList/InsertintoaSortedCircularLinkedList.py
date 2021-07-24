class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
head = Node(3)
l1 = Node(3)
l2 = Node(5)
head.next = l1
l1.next = l2
l2.next = head
insertVal = 0
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if head is None:
            newNode.next = newNode
            return newNode
        else:
            holdHead = head
            while head:
                getCurrvalue = head.val
                getNextValue = head.next.val
                if getNextValue > getCurrvalue:
                    if (getCurrvalue <= insertVal <= getNextValue):
                        holdNext = head.next
                        head.next = newNode
                        newNode.next = holdNext
                        return holdHead
                elif getNextValue < getCurrvalue:
                    if (insertVal <= getNextValue and insertVal <= getCurrvalue) or (
                            insertVal >= getNextValue and insertVal >= getCurrvalue):
                        holdNext = head.next
                        head.next = newNode
                        newNode.next = holdNext
                        return holdHead
                elif getNextValue == getCurrvalue:
                    if holdHead == head.next:
                        holdNext = head.next
                        head.next = newNode
                        newNode.next = holdNext
                        return holdHead
                head = head.next



obj = Solution()
print(obj.insert(head, insertVal))
