class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

#               5
#           /       \
#          6          1
#       /      \        \
#      8        9        3
#            /     \    /
#          10       2  4

root=TreeNode(5)
root.left=TreeNode(6)
root.right=TreeNode(1)

class Solution:
    def __init__(self):
        self.maxAverage = 0
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.average(root)
        return float(self.maxAverage)

    def average(self, root):
        if root is None:
            return [0, 0]
        elif root is not None:
            left= self.average(root.left)
            right= self.average(root.right)
            sum= left[0] + right[0] + root.val
            if left[1]==0 and right[1]==0:
                self.maxAverage=max(self.maxAverage, root.val)
                return [root.val, 1]
            else:
                self.maxAverage= max((sum / (left[1] + right[1] +1)), self.maxAverage)
                return [sum, (left[1] + right[1] +1)]
obj=Solution()
print(obj.maximumAverageSubtree(root))