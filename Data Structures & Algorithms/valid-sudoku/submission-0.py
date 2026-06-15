class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(9)]
        col_sets = [set() for i in range(9)]
        square_sets = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val != '.':
                    if val in row_sets[i]:
                        return False
                    else:
                        row_sets[i].add(val)

                    if val in col_sets[j]:
                        return False
                    else:
                        col_sets[j].add(val)

                    square_ind = 3 * (i // 3) + j // 3

                    if val in square_sets[square_ind]:
                        return False
                    else:
                        square_sets[square_ind].add(val)

        return True