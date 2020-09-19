class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#   S               3                                    t          4
#              /         \                                      /       \
#             4           5                                    1         2
#           /   \
#          1     2
#               /
#              0

# s= TreeNode(3)
# s.left= TreeNode(4)
# s.right= TreeNode(5)
# s.left.left= TreeNode(1)
# s.left.right= TreeNode(2)
# s.left.right.left= TreeNode(0)
#
# t = TreeNode(4)
# t.left = TreeNode(1)
# t.right = TreeNode(2)

#   S               1                                    1
#              /
#             1

s= TreeNode(1)
s.left= TreeNode(1)
t = TreeNode(1)


class Solution:
    def check(self, s, t):
        if s is not None:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None or t is None:
            if s is None and t is None:
                return True
            else:
                return False
        else:
            if s.val == t.val:
                left= self.isSubtree(s.left, t.left)
                right = self.isSubtree(s.right, t.right)
                if left == True and right== True:
                    return True
                else:
                    return False
            elif s.val != t.val:
                left = self.isSubtree(s.left, t)
                right = self.isSubtree(s.right, t)
                if left == True or right == True:
                    return True
                else:
                    return False


obj=Solution()
print(obj.check(s, t))

