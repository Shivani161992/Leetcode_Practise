from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.right.left = TreeNode(2)
root.right.right.left.left = TreeNode(0)
root.right.right.left.right = TreeNode(4)

subRoot=TreeNode(2)
subRoot.left=TreeNode(0)
subRoot.right=TreeNode(4)


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None:
            return False
        else:
            stackRoot=[root]
            subRootTraversal= self.traversal(subRoot)
            seen=set()
            while stackRoot:
                getNode= stackRoot.pop()
                if getNode.val == subRoot.val:
                    traver=self.traversal(getNode)
                    if traver==subRootTraversal:
                        return True
                if getNode.left and getNode.left not in seen:
                    stackRoot.append(getNode.left)
                if getNode.right and getNode.right not in seen:
                    stackRoot.append(getNode.right)
            return False
    def traversal(self, node):
        bfsqueue= deque()
        bfsqueue.append(node)
        pattern=""
        while bfsqueue:
            getNode=bfsqueue.popleft()
            if getNode:
                bfsqueue.append(getNode.left)
                bfsqueue.append(getNode.right)
                pattern = pattern + str(getNode.val) + ','
            else:
                pattern = pattern + 'N' + ','
        return pattern











obj=Solution()
print(obj.isSubtree(root, subRoot))