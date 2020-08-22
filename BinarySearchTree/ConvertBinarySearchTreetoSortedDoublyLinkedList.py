class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

        #                                               4
        #                                            /      \
        #                                           2        5
        #                                        /     \
        #                                       1       3
        #
        #
root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(1)
root.left.right=Node(3)
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        print()

obj=Solution()
obj.treeToDoublyList(root)
