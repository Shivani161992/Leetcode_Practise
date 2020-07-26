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
    def __init__(self   ):
        self.root=root
    #Recursively
    def print_traversal(self, root):
        traversal=""
        print("Preorder Traversal recursively", self.recursive_preorder_traverse(self.root, traversal))
        print("Inorder Traversal recursively", self.recursive_inorder_traverse(self.root, traversal))
        print("Postorder Traversal iteratively", self.recursive_postorder_traverse(self.root, traversal))
    def recursive_preorder_traverse(self, root, traversal):
        if root:
            traversal = traversal + str(root.value) + "--->"
            traversal = self.recursive_preorder_traverse(root.left, traversal)
            traversal = self.recursive_preorder_traverse(root.right, traversal)
        return traversal
    def recursive_inorder_traverse(self, root, traversal):
        if root:
            traversal = self.recursive_inorder_traverse(root.left, traversal)
            traversal = traversal + str(root.value) + "--->"
            traversal = self.recursive_inorder_traverse(root.right, traversal)
        return traversal
    def recursive_postorder_traverse(self, root, traversal):
        if root:
            traversal = self.recursive_postorder_traverse(root.left, traversal)
            traversal = self.recursive_postorder_traverse(root.right, traversal)
            traversal = traversal + str(root.value) + "--->"
        return traversal

    #Iteratively
    def print_traversal_iterative(self, root):
        traversal=''
        print("Preorder Traversal iteratively", self.iterative_preorder_traverse(root, traversal))
        print("Inorder Traversal iteratively", self.iterative_inorder_traverse(root, traversal))
        print("Postorder Traversal iteratively", self.iterative_postorder_traverse(root, traversal))
    def iterative_preorder_traverse(self, root, traversal):
        hold_node=[root]
        while len(hold_node) != 0:
            hold= hold_node.pop()
            traversal = traversal + str(hold.value) + '-->'
            if hold.right:
                hold_node.append(hold.right)
            if hold.left:
                hold_node.append(hold.left)
        return traversal
    def iterative_inorder_traverse(self, root, traversal):
        traversal = []
        hold = [root]
        stack =[]
        while len(hold) != 0:
            get = hold[-1]
            if get.left and get.left not in stack:
                hold.append(get.left)
            else:
                remove = hold.pop()
                stack.append(remove)
                traversal.append(remove.value)

                if remove.right:
                    hold.append(remove.right)

        return traversal
    def iterative_postorder_traverse(self, root, traversal):
        hold=[root]
        stack=[]
        while len(hold) != 0:
            get = hold[-1]
            if get.left and get.left not in stack:
                hold.append(get.left)
            else:
                if get.right and get.right not in stack:
                    hold.append(get.right)
                else:
                    remove= hold.pop()
                    stack.append(remove)
                    traversal = traversal + str(remove.value) + "-->"

        return traversal



obj = Solution()
obj.print_traversal(root)
obj.print_traversal_iterative(root)