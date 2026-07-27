

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i, row in enumerate(matrix):
            contains_zeros = False

            for j, n in enumerate(row):
                if n == 0:
                    contains_zeros = True
                    matrix[i][j] = None

            if contains_zeros:
                for j in range(len(row)):
                    if matrix[i][j] is not None:
                        matrix[i][j] = 0

        for j in range(len(matrix[0])):
            contains_zeros = False

            for i in range(len(matrix)):
                if matrix[i][j] is None:
                    contains_zeros = True

            if contains_zeros:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''for i, row in enumerate(matrix):
            zero_found = False

            for j, n in enumerate(row):
                if n is None:
                    matrix[i][j] = 0
                elif n == 0:
                    zero_found = True

                    vertically_nonadjacent_zeros = 0

                    for offset in (-1, 1):
                        i_new = i + offset

                        if 0 <= i_new < len(matrix) and matrix[i_new][j] != 0:
                            vertically_nonadjacent_zeros += 1

                    if vertically_nonadjacent_zeros != 0:
                        for i_overwrite in range(len(matrix)):
                            matrix[i_overwrite][j] = 0 if i_overwrite <= i or matrix[i_overwrite][j] == 0 else None

            if zero_found:
                row[:] = (0 for _ in range(len(row)))'''