from typing import List
board = [["a","b"],["c","d"]]
words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found=[]
        row= len(board)
        col= len(board[0])
        index=0
        hold=''
        for word in words:
            word_found = False
            for r in range(0, row):
                for c in range(0, col):
                    if board[r][c] == word[0]:
                        word_found= self.search(board, word, hold, r, c, index)
                        if word_found == True:
                            found.append(word)
                            break
                if word_found == True:
                    break
        return found

    def search(self, board, word, hold, r, c, index):
        if r >=0 and r < len(board) and c >=0 and c < len(board[0]) and index < len(word):
            if board[r][c] == word[index]:
                hold = hold + word[index]
                temp = board[r][c]
                board[r][c] = '0'
                if word == hold:
                    board[r][c] = temp
                    return True
                left = self.search(board, word, hold, r, c - 1, index + 1)
                right = self.search(board, word, hold, r, c + 1, index + 1)
                top = self.search(board, word, hold, r - 1, c, index + 1)
                bottom = self.search(board, word, hold, r + 1, c, index + 1)
                board[r][c] = temp

                if left == True or right == True or top == True or bottom == True:
                    return True
                else:
                    return False

        else:
            return False

obj=Solution()
print(obj.findWords(board, words))
