# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
p=5
q=1

root= TreeNode(3)
root.left=TreeNode(5)
root.right=TreeNode(1)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(7)
root.left.right.right=TreeNode(4)

root.right.left=TreeNode(0)
root.right.right=TreeNode(8)

p= root.left
q= root.left.right.right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        else:
            stack=[root]
            seen=[]
            pfound=False
            qfound=False
            lca=None
            traverse=[]

            while len(stack) !=0:
                node=stack[-1]
                if node.val == p.val:
                    pfound=True
                    if lca==None:
                        lca=node
                elif node.val == q.val:
                    qfound=True
                    if lca==None:
                        lca=node
                if pfound==True and qfound ==True:
                    return lca.val
                if node.left and node.left not in seen:
                    stack.append(node.left)
                elif node.right and node.right not in seen:
                    stack.append(node.right)
                else:
                    stack.pop()
                    seen.append(node)
                    traverse.append(node.val)
                    if node==lca:
                        lca=stack[-1]






obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))

