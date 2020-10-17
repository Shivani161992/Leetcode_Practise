from typing import List
word = "AAB"
board =[["C","A","A"],["A","A","A"],["B","C","D"]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        index=0
        hold=''
        for r in range(0, row):
            for c in range(0, col):
                if board[r][c]==word[index]:
                    found = self.search(board, word, hold, index, r, c)
                    if found == True:
                        return True
        return False

    def search(self, board, word, hold, index, r, c):
        if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and index < len(word):
            if board[r][c] == word[index]:
                hold = hold + board[r][c]
                store = board[r][c]
                board[r][c] = 0
                if word == hold:
                    return True
                right = self.search(board, word, hold, index + 1, r, c + 1)
                left = self.search(board, word, hold, index + 1, r, c - 1)
                bottom = self.search(board, word, hold, index + 1, r + 1, c)
                top = self.search(board, word, hold, index + 1, r - 1, c)
                if right == True or left == True or top == True or bottom == True:
                    return True
                else:
                    board[r][c] = store
                    return False
            else:
                return False
        else:
            return False

obj=Solution()
print(obj.exist(board, word))

