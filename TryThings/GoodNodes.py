

def goodNodes(self, root) -> int:
    if root is None:
        return 0
    else:
        maxLevel = root.val
        self.findgoodNodes(root, self.good, maxLevel)
        return self.good


def findgoodNodes(self, root, goodNodes, maxLevel):
    if root:
        if root.val >= maxLevel:
            maxLevel = root.val
            self.good = self.good + 1
        self.findgoodNodes(root.left, self.good, maxLevel)
        self.findgoodNodes(root.right, self.good, maxLevel)
        return
    return