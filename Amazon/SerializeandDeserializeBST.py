class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(33)
root.left = TreeNode(10)
root.right = TreeNode(4)
root.left.left = TreeNode(0)

data = '3140NNNNN'

from collections import deque
class Codec:
    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return ''
        else:
            traversal=''
            bfsqueue= deque()
            bfsqueue.append(root)
            while bfsqueue:
                getElement= bfsqueue.popleft()
                if getElement is not None:
                    traversal= traversal + str(getElement.val) + ','
                    bfsqueue.append(getElement.left)
                    bfsqueue.append(getElement.right)
                else:
                    traversal = traversal + 'N'+','
            return traversal

    def deserialize(self, data: str) -> TreeNode:
        if data != "":
            data= data.split(sep=",")
            root=TreeNode(data[0])
            deserializebfs = deque()
            deserializebfs.append(root)
            i = 1
            while i < len(data) and len(deserializebfs) >0 :
                getelement= deserializebfs.popleft()
                if data[i] !='N':
                    createNode1= TreeNode(data[i])
                    getelement.left= createNode1
                    deserializebfs.append(createNode1)
                if data[i+1] !='N':
                    createNode2 = TreeNode(data[i+1])
                    getelement.right = createNode2
                    deserializebfs.append(createNode2)
                i=i+2
            return root
        else:
            return None

obj = Codec()
print(obj.serialize(root))
print(obj.deserialize(data))
