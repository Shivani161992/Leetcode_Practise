class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#                       1
#                   /       \
#                  2         5
#               /    \         \
#              3      4         6

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(5)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.right=TreeNode(6)

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        else:
            hold_root=root
            hold_right=[]
            while root:
                if root.left is not None:
                    if root.right is not None:
                        hold_right.append(root.right)
                        root.right=root.left
                        root.left= None
                        root = root.right
                    else:
                        root.right = root.left
                        root.left = None
                        root = root.right

            elif root.left is None:
                    if root.right:
                        root= root.right
                    elif root.right is None:
                        if len(hold_right) !=0:
                            root.right= hold_right.pop()
                            root = root.right
                        else:
                            root = root.right
            root= hold_root



obj=Solution()
print(obj.flatten(root))