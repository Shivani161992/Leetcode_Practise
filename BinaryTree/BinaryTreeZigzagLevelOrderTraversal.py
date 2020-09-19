# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        #                                               3
        #                                            /      \
        #                                           9        20
        #                                                  /     \
        #                                                 15      7

root= TreeNode(3)
root.left= TreeNode(9)
root.right= TreeNode(20)
root.right.right= TreeNode(7)
root.right.left= TreeNode(15)

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        tree_queue=[root]
        traverse=[]
        count = 0
        while len(tree_queue) !=0:
            ltree_queue= len(tree_queue)
            group=[]
            for i in range(0, ltree_queue):
                get=tree_queue.pop(0)
                group.append(get.val)
                if get.left:
                    tree_queue.append(get.left)
                if get.right:
                    tree_queue.append(get.right)
            if count ==1:
                traverse.append(group.copy()[::-1])
                count=0
            elif count ==0:
                traverse.append(group.copy())
                count = 1

        return traverse

obj= Solution()
print(obj.zigzagLevelOrder(root))
