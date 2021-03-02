# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#                        3
#                    /       \
#                   4         5
#                /     \
#               1       2
#                     /
#                    0
#
s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
#s.left.right.left = TreeNode(0)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        thead = t
        bool = False
        self.istree(s, t, thead, bool)
        return bool

    def istree(self, s, t, thead, bool):
        if s and t:
            if s.val != t.val:
                bool =False
                self.istree(s.left, t, thead, bool )
                self.istree(s.right, t, thead, bool )
            elif s.val == t.val:
                self.bool =True
                self.istree(s.left, t.left, thead, bool )
                self.istree( s.right, t.right, thead, bool )

        else:
            return







obj = Solution()
print(obj.isSubtree(s, t))
