from typing import List
class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

#                                       F
#                                 /           \
#                               B               G
#                          /       \                 \
#                        A          D                  I
#                              /         \           /
#                             C           E         H

root= Node("F")
root.left = Node('B')
root.right = Node('G')
root.left.left = Node('A')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.left.right.right = Node('E')
root.right.right = Node('I')
root.right.right.left = Node('H')


class Solution:
    def inorderTraversal(self, root: Node) -> List[int]:
        traversal = []
        if root is None:
            return traversal
        else:
            seen = []
            stack = [root]
            while len(stack) != 0:
                get = stack[-1]
                if get.left is not None and get.left not in seen:
                    stack.append(get.left)
                else:
                    traversal.append(get.value)
                    seen.append(get)
                    stack.pop()
                    if get.right is not None and get.right not in seen:
                        stack.append(get.right)
            return traversal

obj=Solution()
print(obj.inorderTraversal(root))