board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if (len(board) == 0):
            return False
        else:
            row = len(board)
            col = len(board[0])
            w = ""
            idx=0
            for r in range(row):
                for c in range(col):
                    if board[r][c]==word[idx]:
                        search= self.search(board, r, c, word, w, idx)
                        if search == True:
                            return search
            return False

    def search(self, board, r, c, word, w, idx):
        if (r>=0 and r < len(board) and c >= 0 and c < len(board[0]) and idx < len(word)):
            if (board[r][c]== word[idx]):
                w = w + word[idx]
                hold = board[r][c]
                board[r][c]=0
                if w == word:
                    return True
                left = self.search(board, r, c-1, word, w, idx+1)
                right = self.search(board, r, c+1, word, w, idx+1)
                top = self.search(board, r-1, c, word, w, idx+1)
                bottom = self.search(board, r+1, c, word, w, idx+1)

                if left==True or right ==True or top== True or bottom==True:
                    return True
                else:
                    board[r][c] = hold
                    return False
            else:
                return False
        else:
            return False




Obj = Solution()
print(Obj.exist(board, word))
