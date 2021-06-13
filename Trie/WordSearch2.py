from typing import List

board = [["o", "a", "a", "n"], ["s", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain", "oats"]


class Trie:
    def __init__(self, c):
        self.char = c
        self.next = dict()
        self.word = ''
        self.isWord = False


class Solution:
    def __init__(self):
        self.getTrie = Trie('/')
        self.wordsFound=[]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.createTrie(self.getTrie, word)
        row= len(board)
        col=len(board[0])
        for r in range(0, row):
            for c in range(0, col):
                cell= board[r][c]
                if cell in self.getTrie.next:
                    holdTrie= self.getTrie
                    self.dfs(board, r, c, holdTrie)

        return self.wordsFound
    def createTrie(self, trie, word):
        holdTrie = trie
        holdWord = ''
        for w in word:
            holdWord = holdWord + w
            if w not in trie.next:
                newNode = Trie(w)
                newNode.word=holdWord
                trie.next[w] = newNode

            if w in trie.next:
                getNode=trie.next[w]
                trie=getNode
                if trie.word== word:
                    trie.isWord=True
        trie=holdTrie
    def dfs(self, board, r, c, trie):
        if r >=0 and r < len(board) and c >= 0 and c < len(board[0]):
            if board[r][c] in trie.next:
                cell=board[r][c]
                if cell==trie.next[cell].char:
                    if trie.next[cell].isWord==True:
                        self.wordsFound.append(trie.next[cell].word)
                    board[r][c]='#'
                    trie= trie.next[cell]
                    self.dfs(board, r+1, c, trie)
                    self.dfs(board, r-1, c, trie)
                    self.dfs(board, r, c+1, trie)
                    self.dfs(board, r, c-1, trie)
                    board[r][c]=cell
                    return


                else:return
            else:return
        else:return






obj = Solution()
print(obj.findWords(board, words))
