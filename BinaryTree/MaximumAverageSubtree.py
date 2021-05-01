class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

#               5
#           /       \
#          6          1
#
#
#
#
#
#
#


root=TreeNode(5)
root.left=TreeNode(6)
root.right=(1)

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        print()