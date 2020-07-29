sum = 1
class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
#                                               5
#                                          /          \
#                                         4            8
#                                      /             /    \
#                                    11             13     4
#                                  /    \                   \
#                                 7      2                   1
#
#
#
#
root=Node(1)
root.left=Node(2)
# root.right=Node(8)
# root.left.left=Node(11)
# root.left.left.left=Node(7)
# root.left.left.right=Node(12)
# root.right.left=Node(13)
# root.right.right=Node(4)
# root.right.right.right=Node(1)


class Solution:
    def hasPathSum(self, root: Node, sum: int) -> bool:
        cal = 0
        result = self.helper(root, sum, cal)
        return result

    def helper(self, root, sum, cal):
        if root is None:
            return 0
        else:
            cal = cal + root.val
            if root.left is None and root.right is None:
                if cal == sum:
                    return True
            else:
                left = self.helper(root.left, sum, cal)
                right = self.helper(root.right, sum, cal)
                if left == True or right == True :
                    return True
                else:
                    return False


obj=Solution()
print(obj.hasPathSum(root, sum))
