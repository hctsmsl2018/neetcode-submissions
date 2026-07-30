class Solution:
    def search_row(self, row):
        if row == self.n:
            board = []

            for queen_col in self.per_row_placements:
                row = []

                for col in range(self.n):
                    row.append("Q" if col == queen_col else ".")

                board.append("".join(row))

            self.solutions.append(board)
        else:
            for col in list(self.unvisited_cols):
                if (row, col) in self.pos_unvisited:
                    self.per_row_placements.append(col)

                    removed = set()

                    for i in self.unvisited_cols:
                        if (row, i) in self.pos_unvisited:
                            self.pos_unvisited.remove((row, i))
                            removed.add((row, i))

                    next_row = row + 1

                    for i in range(next_row, self.n):
                        if (i, col) in self.pos_unvisited:
                            self.pos_unvisited.remove((i, col))
                            removed.add((i, col))

                    indices_sum = row + col

                    for i in range(next_row, self.n):
                        diag_inds = (i, indices_sum - i)

                        if diag_inds in self.pos_unvisited:
                            self.pos_unvisited.remove(diag_inds)
                            removed.add(diag_inds) 

                    indices_diff = row - col

                    for i in range(next_row, self.n):
                        diag_inds = (i, i - indices_diff)

                        if diag_inds in self.pos_unvisited:
                            self.pos_unvisited.remove(diag_inds)
                            removed.add(diag_inds) 

                    self.unvisited_cols.remove(col)

                    self.search_row(row + 1)

                    self.per_row_placements.pop()

                    self.pos_unvisited |= removed

                    self.unvisited_cols.add(col)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.unvisited_cols = set(range(n))
        self.pos_unvisited = {(i, j) for i in range(n) for j in range(n)}
        self.per_row_placements = []
        self.solutions = []
        self.n = n

        self.search_row(0)

        return self.solutions