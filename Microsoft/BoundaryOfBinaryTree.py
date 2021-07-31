from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#                                       1
#                                 /           \
#                               2               3
#                          /       \           /
#                        4          5         6
#                                 /    \    /   \
#                                7      8 9      10

root= TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            leafseen=set(root)
            traverse=[root.val]

            self.getLeftBoundary(root.left, traverse)
            self.getLeafNodes(root, traverse, leafseen)
            self.getRightBoundary(root.right, traverse)
            return traverse

    def getLeftBoundary(self, root, traverse):
        if root:
            stack=[root]
            seen=set()
            while stack:
                getNode= stack.pop()
                seen.add(getNode)
                if getNode.left is not None or getNode.right is not None:
                    traverse.append(getNode.val)
                    if getNode.left is not None:
                        stack.append(getNode.left)
                    elif getNode.right is not None:
                        stack.append(getNode.left)
    def getLeafNodes(self, root, traverse, leafseen):
        if root:
            stack=[root]
            seen=set()
            while stack:
                getNode=stack[-1]
                if getNode.left and getNode.left not in seen:
                    stack.append(getNode.left)
                else:
                    stack.pop()
                    seen.add(getNode)
                    if getNode.left is None and getNode.right is None:
                        if getNode not in leafseen:
                            traverse.append(getNode.val)
                    elif getNode.right and getNode.right not in seen:
                        stack.append(getNode.right)
    def getRightBoundary(self, root, traverse):
        if root:
            stack=[root]
            seen=set()
            while stack:
                getNode=stack[-1]
                if getNode.left is None and getNode.right is None:
                    stack.pop()
                    seen.add(getNode)

                elif getNode.right is None and getNode.left not in seen :
                    if getNode.left and getNode.left not in seen:
                           stack.append(getNode.left)
                elif getNode.right and getNode.right not in seen:
                    stack.append(getNode.right)
                else:
                    stack.pop()
                    seen.add(getNode)
                    traverse.append(getNode.val)



obj=Solution()
print(obj.boundaryOfBinaryTree(root))
