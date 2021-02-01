class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#                                       F
#                                 /           \
#                               B               G
#                          /       \                 \
#                        A          D                  I
#                              /         \           /
#                             C           E         H



#      3
#     / \
#    4   5
#   / \
#  1   2

root= TreeNode("F")
root.left = TreeNode('B')
root.right = TreeNode('G')
root.left.left = TreeNode('A')
root.left.right = TreeNode('D')
root.left.right.left = TreeNode('C')
root.left.right.right = TreeNode('E')
root.right.right = TreeNode('I')
root.right.right.left = TreeNode('H')
from typing import List
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        else:
            traversal=[]
            stack=[root]
            while len(stack) !=0:
                getNode= stack.pop()
                traversal.append(getNode.val)
                if getNode.right:
                    stack.append(getNode.right)
                if getNode.left:
                    stack.append(getNode.left)
            return traversal

    def preorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        traversal=[]
        self.preTraversal(root, traversal)
        return traversal

    def preTraversal(self, root, traversal):
        if root:
            traversal.append(root.val)
            self.preTraversal(root.left, traversal)
            self.preTraversal(root.right, traversal)
            return traversal

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        else:
            traversal=[]
            stack=[root]
            seen=[]
            while len(stack) !=0:
                getNode= stack[-1]
                if getNode.left and getNode.left not in seen:
                    stack.append(getNode.left)
                else:
                    holdNode= stack.pop()
                    traversal.append(holdNode.val)
                    seen.append(holdNode)
                    if getNode.right and getNode.right not in seen:
                        stack.append(getNode.right)
            return traversal

    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        else:
            traversal=[]
            return self.inTraversal(root, traversal)

    def inTraversal(self, root, traversal):
        if root:
            self.inTraversal(root.left, traversal)
            traversal.append(root.val)
            self.inTraversal(root.right, traversal)
            return traversal

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        else:
            traversal=[]
            seen=[]
            stack=[root]
            while len(stack) !=0:
                getNode= stack[-1]
                if getNode.left and getNode.left not in seen:
                    stack.append(getNode.left)
                else:
                    if getNode.right and getNode.right not in seen:
                        stack.append(getNode.right)
                    holdNode= stack.pop()
                    traversal.append(holdNode.val)
                    seen.append(holdNode)

            return traversal

    def preorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        else:
            traversal=[]
            return self.preTraversal(root, traversal)

    def preTraversal(self, root, traversal):
        if root:
            self.preTraversal(root.left, traversal)
            self.preTraversal(root.right, traversal)
            traversal.append(root.val)
            return traversal

    # level order traversal
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        traversal=[]
        if root is None:
            return traversal
        else:
            queue=[root]
            while len(queue) !=0:
                getSize=len(queue)
                group=[]
                for node in range(getSize):
                    getNode= queue.pop(0)
                    group.append(getNode.val)
                    if getNode.left:
                        queue.append(getNode.left)
                    if getNode.right:
                        queue.append(getNode.right)
                traversal.append(group.copy())
            return traversal


        


obj= Solution()
print(obj.levelOrder(root))