from typing import List
class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

        #                                               1
        #                                            /      \
        #                                           2        3
        #                                          /          \
        #                                         4             5
        #                                       /
        #                                      6
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(5)
root.left.left=Node(4)
root.left.left.left=Node(6)
class Solution:
    def rightSideView(self, root: Node) -> List[int]:
        values=[]
        if root is None:
            return values
        else:
            stack = [root]
            while len(stack) != 0:
                stack_length = len(stack)
                values.append(stack[len(stack)-1].val)
                for i in range(0, stack_length):
                    get= stack.pop(0)
                    if get.left is not None:
                        stack.append(get.left)
                    if get.right is not None:
                        stack.append(get.right)

            return values
obj=Solution()
print(obj.rightSideView(root))