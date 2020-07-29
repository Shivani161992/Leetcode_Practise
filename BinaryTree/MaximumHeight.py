class Node:
    def __init__(self, value):
        self.value=value
        self.left = None
        self.right = None


#                                       F
#                                 /           \
#                               B               G
#                                                 \
#                                                   I


root= Node("F")
root.left = Node('B')
root.right = Node('G')
root.right.right = Node('I')


class Solution:
    def maximum_height_iterative(self, root):
            if root is None:
                return
            else:
                hold=[root]
                traversal=[]
                while len(hold) != 0:
                    get=len(hold)
                    group=[]
                    for i in range(0, get):
                        group.append(hold[0].value)
                        if hold[0].left:
                            hold.append(hold[0].left)
                        if hold[0].right:
                            hold.append(hold[0].right)
                        hold.pop(0)

                    traversal.append(group)

                return len(traversal)-1

    def maximum_height_recursive(self, root):
        if root is None:
            return 0
        else:
            left = self.maximum_height_recursive(root.left)
            right= self.maximum_height_recursive(root.right)
            maximum = max(left, right)
            return maximum + 1

obj=Solution()
print(obj.maximum_height_recursive(root))