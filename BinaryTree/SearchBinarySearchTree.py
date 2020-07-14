val=5
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #     4
    #    / \
    #   2   7
    #  / \
    # 1   3
root=TreeNode(4)
root.left= TreeNode(2)
root.right= TreeNode(7)
root.left.left= TreeNode(1)
root.left.right= TreeNode(3)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if (root==None):
            return None
        elif (root.val==val):
            return  root
        elif (root.val>val):
            return  self.searchBST(root.left, val)
        elif (root.val<val):
            return  self.searchBST(root.right, val)




bst=Solution()
y=bst.searchBST(root, val)
print(y)
