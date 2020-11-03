from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val= val
        self.children= children

head=Node(1)
child1=Node(3)
child2=Node(2)
child3=Node(4)

child4=Node(5)
child5=Node(6)

head.children=[child1, child2, child3]
child1.children=[child4, child5]
class Solution:
    # all done iteratively
    def preorder(self, root: 'Node') -> List[int]:
        traversal=[]
        if root is None:
            return traversal
        else:
            stack=[root]
            while len(stack) !=0 :
                get= stack.pop()
                traversal.append(get.val)
                if get.children:
                    for i in range(len(get.children)-1, -1, -1):
                        stack.append(get.children[i])
            return traversal

    def postorder(self, root: 'Node') -> List[int]:
        traversal=[]
        if root is None:
            return traversal
        else:
            stack=[root]

            while len(stack) !=0:
                get= stack[-1]
                if get.children:
                    stack.extend(get.children[::-1])
                    get.children=None

                else:
                    pop_item=stack.pop()
                    traversal.append(pop_item.val)
            return traversal

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        traversal=[]
        if root is None:
            return traversal
        else:
            queue=[root]
            while len(queue) !=0:
                groupl=len(queue)
                group=[]
                for i in range(0, groupl):
                    get= queue.pop(0)
                    group.append(get.val)
                    if get.children:
                        queue.extend(get.children)
                traversal.append(group.copy())
            return traversal

    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        else:
            traversal = []
            queue = [root]
            while len(queue) != 0:
                groupl = len(queue)
                group = []
                for i in range(0, groupl):
                    get = queue.pop(0)
                    group.append(get.val)
                    if get.children:
                        queue.extend(get.children)
                traversal.append(group.copy())
            return len(traversal)


obj=Solution()
print(obj.levelOrder(head))