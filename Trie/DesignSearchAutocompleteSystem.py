from typing import List

sentences = ['abc', 'abbc', 'a']
times = [3,3,3]
["a"],["b"],["c"],["#"],["a"],["b"],["c"],["#"]
class Trie:
    def __init__(self, x):
        self.char = x
        self.prefix = ""
        self.children = {}
        self.isWord = False
        self.wordCount = 0
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie('/')
        self.holdTrie= self.trie
        self.holdWord = ''
        self.sentenceSet=set()
        count = 0
        for sentence in sentences:
            self.sentenceSet.add(sentence)
            self.creatTrie(sentence, times[count])
            count = count + 1
    def input(self, c: str) -> List[str]:
        output = []
        dictionary = {}
        if c != '#':
            self.holdWord = self.holdWord + c
            self.traverse(self.holdWord, dictionary)
        else:
            self.trie=self.holdTrie
            if self.holdWord not in self.sentenceSet:
                self.sentenceSet.add(self.holdWord)
                self.creatTrie(self.holdWord, 1)
            else:
                self.updateTrie(self.holdWord)
            self.holdWord = ''
        dic=sorted(dictionary.items(), key=lambda x : (-x[1], x[0]))
        count=0
        for d in dic:
            count= count + 1
            output.append(d[0])
            if count==3:
                break
        self.trie = self.holdTrie
        return output

    def creatTrie(self, sentence, time):
        word = ""
        for s in sentence:
            word = word + s
            if s not in self.trie.children:
                newNode = Trie(s)
                self.trie.children[s] = newNode
                newNode.prefix = newNode.prefix + word
                if word == sentence:
                    newNode.isWord = True
                    newNode.wordCount = newNode.wordCount +  time
            elif s in self.trie.children:
                getnode= self.trie.children[s]
                if word == sentence:
                    getnode.isWord = True
                    getnode.wordCount = getnode.wordCount + time
            self.trie = self.trie.children[s]
        self.trie = self.holdTrie

    def traverse(self, word, dictionary):
        for l in word:
            if l in self.trie.children:
                getChild= self.trie.children[l]
                self.trie= getChild
        x= self.trie
        if self.trie.prefix != self.holdWord:
            return
        self.bfs(dictionary, self.trie)

    def bfs(self, dictionary, node):
        if node.isWord==True:
            dictionary[node.prefix]=node.wordCount
        getChildren= node.children
        for child in getChildren:
            self.bfs(dictionary, getChildren[child])
        return

    def updateTrie(self, sentence):
        word = ""
        for s in sentence:
            word = word + s
            self.trie = self.trie.children[s]
        if word == self.trie.prefix:
            self.trie.wordCount=  self.trie.wordCount + 1

        self.trie = self.holdTrie

obj = AutocompleteSystem(sentences, times)
print(obj.input('b')) #[]
print(obj.input('c')) #[]
print(obj.input('#')) #[]
print(obj.input('b')) #[bc]
print(obj.input('c')) #[bc]
print(obj.input('#')) #[]
print(obj.input('a'))
print(obj.input('b'))
print(obj.input('c'))
print(obj.input('#'))
print(obj.input('a'))
print(obj.input('b'))
print(obj.input('c'))
print(obj.input('#'))

