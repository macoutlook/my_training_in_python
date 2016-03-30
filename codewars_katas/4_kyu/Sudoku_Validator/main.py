class Sudoku(object):

    def __init__(self, board):
        self.board = board

    def is_valid(self):
        if sum([len(row) for row in self.board]) == len(self.board) ** 2 and type(self.board[0][0]) == int:
            digits = set(range(1, len(self.board) +1))
            mod = int(len(self.board) ** 0.5)
            first = True
            for i, row in enumerate(self.board):
                if not set(row) == digits:
                    return False
                for j, el in enumerate(row):
                    if first:
                        col = [item[j] for item in self.board]
                    if not set(col) == digits:
                        return False
                    if i % mod == 0 and j % mod == 0:
                        a = [el[j:j+mod] for el in self.board[i:i+mod]]
                        set_sq = set()
                        for ind in range(len(a)):
                            set_sq |= set(a[ind])
                        if not set_sq == digits:
                            return False
                first = False
        else:
            return False
        return True


def main():
    goodSudoku1 = Sudoku([
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [2, 3, 1, 5, 6, 4, 8, 9, 7],
                          [3, 1, 2, 6, 4, 5, 9, 7, 8],
                          [4, 5, 6, 7, 8, 9, 1, 2, 3],
                          [5, 6, 4, 8, 9, 7, 2, 3, 1],
                          [6, 4, 5, 9, 7, 8, 3, 1, 2],
                          [7, 8, 9, 1, 2, 3, 4, 5, 6],
                          [8, 9, 7, 2, 3, 1, 5, 6, 4],
                          [9, 7, 8, 3, 1, 2, 6, 4, 5]])
    print goodSudoku1.is_valid()


if __name__ == '__main__':
    main()