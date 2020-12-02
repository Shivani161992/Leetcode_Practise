class Node:
    def __init__(self, val):
        self.val=val
        self.children={}
        self.flag=False

class Trie:

    def __init__(self):
        self.trietree=Node('')

    def insert(self, word: str) -> None:
        node= self.trietree
        count = 0
        flag= len(word)
        for w in word:
            count = count +1
            if w not in node.children.keys():
                newnode= Node(w)
                node.children[w]= newnode
                node = newnode
            elif w in node.children.keys():
                node= node.children[w]
            #set the flag TRUE by the end of the word
            if count == flag:
                node.flag=True
        """
        Inserts a word into the trie.
        """

    def search(self, word: str) -> bool:
        count = 0
        flag = len(word)
        node= self.trietree
        for w in word:
            count = count + 1
            if w in node.children.keys():
                node= node.children[w]
            elif w not in node.children.keys():
                return False
            if count == flag and node.flag==True:
                return True
        return node.flag
    def startsWith(self, prefix: str) -> bool:
        node = self.trietree
        for p in prefix:
            if p in node.children.keys():
                node = node.children[p]
            elif p not in node.children.keys():
                return False
        return True




trie = Trie()
trie.insert("apple")
print(trie.search("apple")) #true
print(trie.search("app")) #false
print(trie.startsWith("app")) #true
trie.insert("app");
print(trie.search("app")) #true
