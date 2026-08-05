class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._above_left_sums = []

        for i, row in enumerate(matrix):
            sum_row = []

            for j, n in enumerate(row):
                cell_val = n

                if i != 0:
                    cell_val += self._above_left_sums[-1][j]

                if j != 0:
                    cell_val += sum_row[-1]

                if i != 0 and j != 0:
                    cell_val -= self._above_left_sums[-1][j - 1]

                sum_row.append(cell_val)

            self._above_left_sums.append(sum_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = self._above_left_sums[row2][col2]

        if row1 != 0:
            region_sum -= self._above_left_sums[row1 - 1][col2]

        if col1 != 0:
            region_sum -= self._above_left_sums[row2][col1 - 1]

        if row1 != 0 and col1 != 0:
            region_sum += self._above_left_sums[row1 - 1][col1 - 1]

        return region_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)