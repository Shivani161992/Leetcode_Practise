from typing import List

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
#                                  /    \                /    \
#                                 7      2              5      1
#
#
#
#
root=Node(1)
root.left=Node(2)
root.right=Node(8)
root.left.left=Node(11)
root.left.left.left=Node(7)
root.left.left.right=Node(2)
root.right.left=Node(13)
root.right.right=Node(4)
root.right.right.left=Node(4)
root.right.right.right=Node(1)

sum = 22

# output= [[5,4,11,2], [5,8,4,5]]

class Solution:
    def pathSum(self, root: Node, sum: int) -> List[List[int]]:
        output=[]
        group = []
        result=self.helper(self,root, sum, output, group)
        return result

    def helper(self, root, sum, output, group):
        if root is None:
            return False
        else:
            sum = sum - root.val
            group.append(root.val)
            if root.left is None and root.right is None:
                if sum == 0:
                    output.append(group.copy)
                    return True
            else:
                left = self.helper(root.left, sum, output, group)
                right = self.helper(root.right, sum, output, group)
                if left == True or right== True:
                    output.append(group.copy)
                else:
                    return False


obj= Solution()
print(obj.pathSum(root, sum))