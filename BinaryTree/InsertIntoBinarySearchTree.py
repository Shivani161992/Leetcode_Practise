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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        hold=root
        prev=''
        newnode=TreeNode(val)
        x=self.helo(self, root, val, prev, newnode)
        return hold

    def helo(self, root, val, prev, newnode):
        if (root is None):
            if val < prev.val:
                prev.left = newnode
            elif val > prev.val:
                prev.right = newnode

        elif (val < root.val):
            prev = root
            return self.helo(root.left, val, prev, newnode)
        elif (val > root.val):
            prev = root
            return self.helo(root.right, val, prev, newnode)


bst=Solution()
y=bst.insertIntoBST(root, val)
print(y)

