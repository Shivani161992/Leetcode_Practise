from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

nums = [0, 1, 2, 3, 4, 5]
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        left=0
        right=len(nums)
        root=None
        return self.getmiddle(nums, left, right, root)


    def getmiddle(self, nums, left, right, root):
        if right < left or left > right:
            return root
        else:
            mid= int((left + right) /2)
            if mid != len(nums):
                node = TreeNode(nums[mid])
                if root is None:
                    root=node
                else:
                    self.create_bst(root, node)
                self.getmiddle(nums, left, mid-1, root)
                self.getmiddle(nums, mid+1, right, root)
            return root

    def create_bst(self, root, node):
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                self.create_bst(root.left, node)
        elif root.val < node.val:
            if root.right is None:
                root.right=node
            else:
                self.create_bst(root.right, node)






obj=Solution()
obj.sortedArrayToBST(nums)