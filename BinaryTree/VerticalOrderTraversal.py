from typing import List
from collections import defaultdict
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        else:
            traversal=[]
            vertical=defaultdict(list)
            bfs= deque()
            bfs.append([root, 0])
            while bfs:
                getNode= bfs.popleft()
                vertical[getNode[1]].append(getNode[0].val)
                if getNode[0].left is not None:
                    bfs.append([getNode[0].left, getNode[1]-1])
                if getNode[0].right is not None:
                    bfs.append([getNode[0].right, getNode[1]+1])
            sortByKey= sorted(vertical.keys())
            for i in sortByKey:
                traversal.append(vertical[i].sort())

            return traversal











obj=Solution()
print(obj.verticalTraversal(root))
