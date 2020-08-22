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



class Solution:
    def hasPathSum(self, root: Node, sum: int) -> bool:
        cal = 0
        result = self.helper(root, sum, cal)
        return result

    def helper_recursive(self, root, sum, cal):
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

    def hasPathSum_iterative(self, root, sum: int) -> bool:
        cal = 0
        hold = [root]
        seen = []
        while len(hold) != 0:
            get = hold[-1]
            cal=cal + get.val
            if get.left is not None and get.left not in seen:
                hold.append(get.left)
            elif get.right is not None and get.right not in seen:
                hold.append(get.right)
            elif get.left is None and get.right is None:
                if cal == sum:
                    return True
                else:
                    if len(hold) == 1:
                        cal = cal - get.val
                    else:
                        second = hold[-2]
                        cal = cal - (get.val + second.val)
                    seen.append(get)
                    hold.pop()
            else:
                if len(hold) == 1:
                    cal = cal - get.val
                else:
                    second = hold[-2]
                    cal = cal - (get.val + second.val)
                seen.append(get)
                hold.pop()

        return False





obj=Solution()
#print(obj.hasPathSum(root, sum))
print(obj.hasPathSum_iterative(root, sum))
