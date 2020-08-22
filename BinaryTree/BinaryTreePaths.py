from typing import List

class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

        #                                               1
        #                                            /      \
        #                                           2        3
        #                                            \
        #                                             5

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(5)
class Solution:
    def binaryTreePaths(self, root: Node) -> List[str]:
        output=[]
        group=""
        return self.helper(root, output, group)

    def helper(self, root, output, group):
        if root is None:
            return output
        else:
            group = group + str(root.val) + '->'
            if root.left is None and root.right is None:
                output.append(group[:-2])
                return output
            else:
                left = self.helper(root.left, output, group)
                right = self.helper(root.right, output, group)
                return output

obj=Solution()
print(obj.binaryTreePaths(root))