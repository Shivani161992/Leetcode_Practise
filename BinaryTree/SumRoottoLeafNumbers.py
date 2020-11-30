class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right= None

#               4
#           /       \
#          9         0
#      /      \
#     5        1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(1)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            root_leaf=[]
            elements=0
            self.dfs(root, root_leaf, elements)
            return sum([int(i) for i in root_leaf])

    def dfs(self, root, root_leaf, elements):
        if root is None:
            return False
        elif root:
            elements = elements + str(root.val)
            left= self.dfs(root.left, root_leaf, elements)
            right= self.dfs(root.right, root_leaf, elements)
            if left == False and right == False:
                root_leaf.append(str(elements))


obj=Solution()
print(obj.sumNumbers(root))
