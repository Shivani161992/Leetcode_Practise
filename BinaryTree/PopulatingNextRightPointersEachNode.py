class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
        self.next=None

        #                                               1
        #                                            /      \
        #                                           2        3
        #                                        /     \   /    \
        #                                       4       5  6     7
        #
        #
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return root
        else:
            stack=[root]
            while len(stack) !=0:
                stack_length=len(stack)
                for i in range(0, stack_length):
                    get =   stack.pop(0)
                    if i != stack_length - 1:
                        get.next=stack[0]
                    elif i == stack_length - 1:
                        get.next=None
                    if get.left is not None:
                        stack.append(get.left)
                    if get.right is not None:
                        stack.append(get.right)
            return root


obj=Solution()
x=obj.connect(root)