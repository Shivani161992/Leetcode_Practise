class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

#                                       F
#                                 /           \
#                               B               G
#                          /       \                 \
#                        A          D                  I
#                              /         \           /
#                             C           E         H

root= Node("F")
root.left = Node('B')
root.right = Node('G')
root.left.left = Node('A')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.left.right.right = Node('E')
root.right.right = Node('I')
root.right.right.left = Node('H')

class Solution:
    def __init__(self, root):
        self.root=root

    def print_traversal(self, root):
        traversal=""
        preorder = self.preorder(root, traversal)
        inorder= self.inorder(root, traversal)
        postorder = self.postorder(root, traversal)
        print('Preorder ->', preorder, 'Inorder', inorder, 'Postorder', postorder)

    def preorder(self, root, traversal):
        if root :
            traversal = traversal + str(root.value) + '-'
            traversal = self.preorder(root.left, traversal)
            traversal = self.preorder(root.right, traversal)
        return traversal

    def inorder(self, root, traversal):
        if root is not None:
            traversal= self.inorder(root.left, traversal)
            traversal= traversal + str(root.value) + '-'
            traversal = self.inorder(root.right, traversal)
        return traversal

    def postorder (self, root, traversal):
        if root is not None:
            traversal= self.postorder(root.left, traversal)
            traversal = self.postorder(root.right, traversal)
            traversal = traversal + str(root.value) + '-'
        return traversal

    def print_iteratively(self, root):
        preorder = self.itera_preorder(root)
        inorder = self.itera_inorder(root)
        print("Iteratively Preorder", preorder)
        print("iteratively Inorder", inorder)

    def itera_preorder(self, root):
        if root is None:
            return
        else:
            traversal=''
            hold = [root]
            while len(hold) !=0:
                x=hold.pop()
                traversal= traversal + str(x.value) + '-'
                if x.right is not None:
                    hold.append(x.right)
                if x.left is not None:
                    hold.append(x.left)
            return traversal

    def itera_inorder(self, root):
        if root is None:
            return
        else:
            inorder_traversal=[]
            hold=[root]
            while len(hold) != 0:
                x=hold[-1]

                if x.left is not None :
                    hold.append(x.left)
                else:
                    y= hold.pop()
                    inorder_traversal.append(y.value)
                    if y.right is not None:
                        hold.append(y.right)
            return inorder_traversal






o=Solution(root)
#print(o.print_traversal(root))
print(o.print_iteratively(root))



