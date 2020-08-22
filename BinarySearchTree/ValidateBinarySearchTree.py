class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None


        #                                               5
        #                                            /    \
        #                                           1      4
        #                                                /   \
        #                                               3     7
        #
root=TreeNode(5)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(7)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        elif root is not None:
            traverse=[]
            seen=[]
            stack =[root]
            while len(stack) !=0:
                get = stack[len(stack)-1]
                if get.left and get.left not in seen:
                    stack.append(get.left)
                else:
                    stack.pop()
                    if len(traverse) != 0:
                        if get.val < traverse[len(traverse) - 1]:
                            return False
                    traverse.append(get.val)
                    seen.append(get)
                    if get.right:
                        stack.append(get.right)

            return True


obj=Solution()
print(obj.isValidBST(root))
