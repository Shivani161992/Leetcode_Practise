class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

root=TreeNode(2)
p=root

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        else:
            found = False
            traverse = []
            stack = [root]
            seen = set()
            while len(stack) != 0:
                getNode = stack[-1]
                if getNode.left and getNode.left not in seen:
                    stack.append(getNode.left)
                else:
                    stack.pop()
                    seen.add(getNode)
                    traverse.append(getNode.val)
                    if getNode.val == p.val and found == False:
                        found = True
                    elif getNode.val != p.val and found == True:
                        return getNode

                    if getNode.right and getNode.right not in seen:
                        stack.append(getNode.right)

            return None

obj=Solution()
print(obj.inorderSuccessor(root, p))