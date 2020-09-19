# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#                           3
#                       /       \
#                      1         4
#                       \
#                         2
#
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right= TreeNode(2)
k=1
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return root
        else:
            ind = 0
            traverse = []
            seen = []
            stack = [root]
            while len(stack) != 0:
                get = stack[len(stack) - 1]
                if get.left is not None and get.left not in seen:
                    stack.append(get.left)
                else:
                    stack.pop()
                    traverse.append(get.val)
                    seen.append(get)
                    ind = ind + 1
                    if ind == k:
                        return get.val
                    if get.right is not None:
                        stack.append(get.right)

obj=Solution()
print(obj.kthSmallest(root, k))

