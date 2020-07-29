class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

root=Node(2)
root.left=Node(3)
root.right=Node(3)

root.left.left=Node(4)
root.left.right=Node(5)

root.right.left=Node(5)
root.right.right=Node(4)




class Solution:
    def symmetric_tree(self, root):
        if root is None:
            return
        else:
            hold=[root]
            traversal=[]
            while len(hold) !=0:
                get=len(hold)
                group=[]
                for i in range(0, get):
                    if hold[0] != None:
                        group.append(hold[0].val)
                        if hold[0].left is None and hold[0].right is None:
                            hold.append(None)
                            hold.append(None)
                        if hold[0].left:
                            hold.append(hold[0].left)
                            if hold[0].right is None:
                                hold.append(None)
                        if hold[0].right:
                            if hold[0].left is None:
                                hold.append(hold[0].left)
                            hold.append(hold[0].right)
                    else:
                        group.append(None)
                    hold.pop(0)
                traversal.append(group)

            for i in traversal:
                if i != i[::-1]:
                    return False
            return True



obj=Solution()
print(obj.symmetric_tree(root))
