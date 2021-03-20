# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


p = 5
q = 1

root = TreeNode(0)
root.left = TreeNode(2)
root.right = TreeNode(1)

root.right.left = TreeNode(3)

target = root.right.left
k = 3


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        allnodes=[]
        if root is None:
            return allnodes
        else:
            stack = [root]
            seendfs = []
            while len(stack) != 0:
                node = stack[-1]
                if node.val == target.val:
                    break
                if node.left and node.left not in seendfs:
                    stack.append(node.left)
                elif node.right and node.right not in seendfs:
                    stack.append(node.right)
                else:
                    stack.pop()
                    seendfs.append(node)


            count=-1
            val=-1
            seen=[]

            while len(stack)!=0:
                holdNode=stack.pop()  #5
                queue=[holdNode] #[5]
                seen.append(holdNode) #[5]
                count = count + 1
                while len(queue) !=0:
                    group_size =len(queue)
                    group=[]
                    val=val+1
                    for q in range(0, group_size):
                        getnode=queue.pop(0)
                        group.append(getnode.val)
                        if getnode.left and getnode.left not in seen:
                            queue.append(getnode.left)
                        if getnode.right and getnode.right not in seen:
                            queue.append(getnode.right)
                    if val == K:
                        allnodes.extend(group.copy())
                        break
                val = count
            return allnodes






    def height(self, root: TreeNode) -> int:
        binarytree = self.treeHeight(root)
        return binarytree

    def treeHeight(self, root):
        if root:
            left = self.treeHeight(root.left)
            right = self.treeHeight(root.right)
            height = max(left, right)
            return height + 1
        else:
            return 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            print()

    def diameter(self, root):
        if root:
            print()


obj = Solution()
print(obj.distanceK(root, target, k))
