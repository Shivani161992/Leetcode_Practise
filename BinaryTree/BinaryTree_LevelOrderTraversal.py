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
from typing import List
class Solution:
    def print_traversal(self, root):
        traversal=[]
        print('Level order traversal', self.levelOrder_traversal(root, traversal))

    def levelOrder_traversal(self, root, traversal):
        if root is None:
            return
        else :
            hold=[root]
            while len(hold) != 0:
                get = len(hold)
                group=[]
                for i in range(0, get):
                    group.append(hold[0].value)
                    if hold[0].left:
                        hold.append(hold[0].left)
                    if hold[0].right:
                        hold.append(hold[0].right)
                    hold.pop(0)
                traversal.append(group)
            return traversal

    def preorderTraversalRecursive(self, root: Node) -> List[int]:
        traversal = []
        self.preTraversal(root, traversal)
        return traversal

    def preTraversal(self, root, traversal):
        if root:
            traversal.append(root.value)
            self.preTraversal(root.left, traversal)
            self.preTraversal(root.right, traversal)
            return traversal

obj= Solution()
print(obj.preorderTraversalRecursive(root))
