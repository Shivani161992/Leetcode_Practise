
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


l1=Node(7, None, None)
l2=Node(13, None, None)
l3=Node(11, None, None)
l4=Node(10, None, None)
l5=Node(1, None, None)

l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5

# connect all randoms
l1.random=None
l2.random=l1
l3.random=l5
l4.random=l3
l5.random=l1

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        store_mapping={}
        hold_nextptr=None
        hold_random_ptr=None
        hold_head=head
        while head:
            #from our head remove all connection
            hold_nextptr=head.next
            hold_random_ptr=head.random

            #remove all connections
            head.next=None
            head.random=None

            #create copy and add it in the hash map
            newnode= Node(head.val, None, None)
            store_mapping[head]=newnode

            #restore all connections
            head.next = hold_nextptr
            head.random = hold_random_ptr
            # go to next pointer
            head=head.next

        head=hold_head
        # create all connections
        while head:
             # get deep copy element
            deep_copy_node= store_mapping[head]

            #assign next pointer to deep_copy
            if head.next:
                get_next= store_mapping[head.next]
                deep_copy_node.next=get_next
            else:
             deep_copy_node.next = None

            #assign random pointer to deep_copy
            if head.random:
                get_random= store_mapping[head.random]
                deep_copy_node.random = get_random
            else:
                deep_copy_node.random = None

            head=head.next

        x= store_mapping[hold_head]


        return store_mapping[hold_head]

obj=Solution()
print(obj.copyRandomList(l1))
