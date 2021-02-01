class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

root=TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)

root.left.left=TreeNode(1)
root.left.right=TreeNode(3)

root.right.left=TreeNode(6)
root.right.right=TreeNode(9)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        else:
            hold_head = root
            stack = [root]
            while len(stack) != 0:
                get_node = stack.pop()
                #                 check if the node any of the child is not None then swap the children
                if get_node.left or get_node.right:
                    hold_left = get_node.left
                    get_node.left = get_node.right
                    get_node.right = hold_left

                if get_node.right:
                    stack.append(get_node.right)
                if get_node.left:
                    stack.append(get_node.left)

            return hold_head

obj=Solution()
obj.invertTree(root)
