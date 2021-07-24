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

p = 2
q = 9


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        else:
            foundp = False
            foundq = False
            stack = [root]
            seen = set()
            lca = None
            while stack:
                getNode = stack[-1]
                if getNode.val == p:
                    foundp = True
                    if lca == None:
                        lca = getNode
                if getNode.val == q:
                    foundq = True
                    if lca == None:
                        lca = getNode
                if foundp == True and foundq == True:
                    return lca.val
                if getNode.left and getNode.left not in seen:
                    stack.append(getNode.left)
                elif getNode.right and getNode.right not in seen:
                    stack.append(getNode.right)
                else:
                    stack.pop()
                    seen.add(getNode)
                    if getNode.val == p or getNode.val == q:
                        lca = stack[-1]

obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))
