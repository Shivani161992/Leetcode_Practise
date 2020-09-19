class Node:
    def __init__(self, value):
        self.value=value
        self.left = None
        self.right = None


#                                       F
#                                 /           \
#                               B               G
#                                                 \
#                                                   I


root= Node("F")
root.left = Node('B')


class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0
        else:
            left= self.maxDepth(root.left)
            right= self.maxDepth(root.right)
            maximum= min (left, right)
            return maximum + 1




obj = Solution()
print(obj.maxDepth(root))


