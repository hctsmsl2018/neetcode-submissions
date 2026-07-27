class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        remainder_v = len(matrix) - 1
        horiz_range = (len(matrix) + 1) // 2

        for i in range(len(matrix) // 2):
            remainder_h = len(matrix) - 1

            for j in range(horiz_range):
                matrix[i][j], matrix[j][remainder_v], matrix[remainder_v][remainder_h], matrix[remainder_h][i] = matrix[remainder_h][i], matrix[i][j], matrix[j][remainder_v], matrix[remainder_v][remainder_h]

                remainder_h -= 1

            remainder_v -= 1