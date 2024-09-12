class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n]*n
        self.r = [0 for _ in range(n)]
        self.c = [0 for _ in range(n)]
        self.diagonal = [0 for _ in range(2)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.r[row] += 1
            self.c[col] += 1
            if row == col:
                self.diagonal[0] += 1
            if row + col == self.n - 1:
                self.diagonal[1] += 1
        else:
            self.r[row] -= 1
            self.c[col] -= 1
            if row == col:
                self.diagonal[0] -= 1
            if row + col == self.n - 1:
                self.diagonal[1] -= 1

        print(self.r)
        print(self.c)
        print(self.diagonal)
        print("**************")
        if self.r[row] == self.n or self.c[col] == self.n or self.diagonal[0] == self.n or self.diagonal[1] == self.n:
                return 1
        if self.r[row] == -self.n or self.c[col] == -self.n or self.diagonal[0] == -self.n or self.diagonal[1] == -self.n:
                return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
