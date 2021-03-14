n = 3


class TicTacToe:
    def __init__(self, n: int):
        self.board = [[None for i in range(n)] for j in range(n)]
        self.diagonal1 = []
        self.r1 = 0
        self.c1 = 0
        while self.r1 < n and self.c1 < n:
            self.diagonal1.append([self.r1, self.c1])
            self.r1 = self.r1 + 1
            self.c1 = self.c1 + 1

        self.diagonal2 = []
        self.r2 = 0
        self.c2 = n - 1
        while self.r2 < n and self.c2 >= 0:
            self.diagonal2.append([self.r2, self.c2])
            self.r2 = self.r2 + 1
            self.c2 = self.c2 - 1

    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] == None:
            if player == 1:
                dia1 = True
                dia2 = True
                row1 = True
                col1 = True
                diag = ""
                player1 = "X"
                self.board[row][col] = player1
                if [row, col] in self.diagonal1:
                    diag = "Diagonal 1"
                    for dia in self.diagonal1:
                        r = dia[0]
                        c = dia[1]
                        if self.board[r][c] != "X":
                            dia1 = False
                    if dia1 == True:
                        return player
                if [row, col] in self.diagonal2:
                    diag = "Diagonal 2"
                    for dia in self.diagonal2:
                        r = dia[0]
                        c = dia[1]
                        if self.board[r][c] != "X":
                            dia2 = False
                    if dia2 == True:
                        return player

                boardRow = len(self.board)
                boardCol = len(self.board[0])
                # iterating over row
                for c in range(0, boardCol):
                    if self.board[row][c] != "X":
                        row1 = False
                if row1 == True:
                    return player

                # iterating over col
                for r in range(0, boardRow):
                    if self.board[r][col] != "X":
                        col1 = False
                if col1 == True:
                    return player
                if (diag == "Diagonal 2"):
                    return 0 if dia2 == False and row1 == False and col1 == False else player
                elif (diag == "Diagonal 1"):
                    return 0 if dia1 == False and row1 == False and col1 == False else player
                else:
                    return 0 if row1 == False and col1 == False else player

            elif player == 2:
                dia1 = True
                dia2 = True
                row1 = True
                col1 = True
                player2 = "O"
                diag = ""
                self.board[row][col] = player2
                if [row, col] in self.diagonal1:
                    diag = "Diagonal 1"
                    for dia in self.diagonal1:

                        r = dia[0]
                        c = dia[1]
                        if self.board[r][c] != "O":
                            dia1 = False
                    if dia1 == True:
                        return player

                if [row, col] in self.diagonal2:
                    diag = "Diagonal 2"
                    for dia in self.diagonal2:
                        r = dia[0]
                        c = dia[1]
                        if self.board[r][c] != "O":
                            dia2 = False
                    if dia2 == True:
                        return player

                boardRow = len(self.board)
                boardCol = len(self.board[0])
                # iterating over row
                for c in range(0, boardCol):
                    if self.board[row][c] != "O":
                        row1 = False
                if row1 == True:
                    return player

                # iterating over col
                for r in range(0, boardRow):
                    if self.board[r][col] != "O":
                        col1 = False

                if col1 == True:
                    return player
                if (diag == "Diagonal 2"):
                    return 0 if dia2 == False and row1 == False and col1 == False else player
                elif (diag == "Diagonal 1"):
                    return 0 if dia1 == False and row1 == False and col1 == False else player
                else:
                    return 0 if row1 == False and col1 == False else player


tictactoe = TicTacToe(n)
print(tictactoe.move(0, 0, 1))
print(tictactoe.move(0, 2, 2))
print(tictactoe.move(2, 2, 1))
print(tictactoe.move(1, 1, 2))
print(tictactoe.move(2, 0, 1))
print(tictactoe.move(1, 0, 2))
print(tictactoe.move(2, 1, 1))
