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
root=Node(5)
root.left=Node(4)
root.right=Node(8)
root.left.left=Node(11)
root.left.left.left=Node(7)
root.left.left.right=Node(2)
root.right.left=Node(13)
root.right.right=Node(4)
root.right.right.left=Node(5)
root.right.right.right=Node(1)

ssum = 22

# output= [[5,4,11,2], [5,8,4,5]]

class Solution:
    def pathSum(self, root: Node, ssum: int) -> List[List[int]]:
        cal = 0
        output=[]
        group=''
        return self.helper(root, ssum,  output, group, cal)

    def helper(self, root, ssum, output, group, cal):
        if root is None:
            return output
        else:
            group= group + str(root.val) + ','
            cal = cal + root.val
            if root.left is None and root.right is None:
                if cal == ssum:
                    x=group.split(',')
                    y= [int(i) for i in x[:-1]]
                    output.append(y)
                    return output
                else:

                    return output
            left = self.helper(root.left, ssum, output, group, cal)
            right = self.helper(root.right, ssum, output, group, cal)
            return output

obj=Solution()
print(obj.pathSum(root, ssum))
