from typing import List

products = ["havana"]
searchWord = "tatiana"


class Trie:
    def __init__(self, x):
        self.val = x
        self.isWord = False
        self.children = {}
        self.prefix = ''


class Solution:
    def __init__(self):
        self.trie = Trie('/')
        self.holdTrie = self.trie

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if len(products) > 0:
            for product in products:
                self.creatTrie(product)
            suggestion = []
            for s in searchWord:
                if s in self.trie.children:
                    holdList = []
                    holdTrie = self.trie.children[s]
                    self.trie= self.trie.children[s]
                    output=self.traverse(self.trie, suggestion, holdList)
                    lexi=sorted(output)
                    suggestion.append(lexi[:3].copy())
                    self.trie= holdTrie
                else:
                    suggestion.append([])

            return suggestion

    def traverse(self, node, suggestion, holdList):
        if node.isWord==True:
            holdList.append(node.prefix)
        getNodechild= node.children
        for child in getNodechild:
            getnode=node.children[child]
            self.traverse(getnode, suggestion, holdList)
        return holdList

    def creatTrie(self, product):
        word = ""
        for p in product:
            word = word + p
            if p not in self.trie.children:
                newNode = Trie(p)
                newNode.prefix = word
                self.trie.children[p] = newNode
                if word == product:
                    newNode.isWord = True
            elif p in self.trie.children:
                getNode = self.trie.children[p]
                if getNode.prefix == product:
                    getNode.isWord = True
            self.trie = self.trie.children[p]
        self.trie = self.holdTrie


obj = Solution()
print(obj.suggestedProducts(products, searchWord))
