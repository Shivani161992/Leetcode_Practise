class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

root=Node(5)
root.left=Node(1)
root.right=Node(5)
root.left.left=Node(5)
root.left.right=Node(5)
root.right.right=Node(5)

class Solution:
    def countUnivalSubtrees(self, root: Node) -> int:
        cal = 0
        count = self.helper(root, cal)
        return count

    def helper(self, root, cal):
        if root is None:
            return
        else:
            return


obj = Solution()
obj.countUnivalSubtrees(root)
