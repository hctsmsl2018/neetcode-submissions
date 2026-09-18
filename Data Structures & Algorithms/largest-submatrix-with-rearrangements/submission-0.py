'''
100
211
321
'''

class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        max_submatrix_area = 0 # 4

        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if i != 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]

        for i, row in enumerate(matrix):
            row.sort(reverse=True)

            height = row[0]

            for j, n in enumerate(row):
                if height != n:
                    max_submatrix_area = max(max_submatrix_area, height * j)
                    height = n

            max_submatrix_area = max(max_submatrix_area, height * len(row))

        return max_submatrix_area