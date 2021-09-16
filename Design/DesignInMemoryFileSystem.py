from typing import List
path=''
filePath=''
content=''

class Node:
    def __init__(self, val):
        self.val=val
        self.children = dict
        self.prefix=''
        self.isFile=False
class FileSystem:
    def __init__(self):
        self.root=Node('/')
        self.trie=self.root

    def ls(self, path: str) -> List[str]:
        directories= path.split(sep='/')

    def mkdir(self, path: str) -> None:
        print()

    def addContentToFile(self, filePath: str, content: str) -> None:
        print()

    def readContentFromFile(self, filePath: str) -> str:
        print()

# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
param_1 = obj.ls(path)
obj.mkdir(path)
obj.addContentToFile(filePath,content)
param_4 = obj.readContentFromFile(filePath)