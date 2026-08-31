class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        prev_row = [] # 1, 0, 0, 1, 0
        largest_area = 0 # 2

        for i in matrix[0]:
            int_i = int(i)
            prev_row.append(int_i)
            largest_area = max(largest_area, int_i)

        for row in islice(matrix, 1, len(matrix)):
            curr_row = [] # 

            for i, n in enumerate(row):
                if i == 0:
                    int_n = int(n)

                    largest_area = max(largest_area, int_n)
                    curr_row.append(int_n)
                elif n == "1":
                    largest_square = min(curr_row[-1], prev_row[i], prev_row[i - 1]) + 1
                    largest_area = max(largest_area, largest_square)
                    curr_row.append(largest_square)
                else:
                    curr_row.append(0)
                    
            prev_row = curr_row

        return largest_area ** 2
        '''prefix_sum_matrix = []

        for row in matrix:
            prefix_sum_row = []

            for i, n in enumerate(row):
                curr_prefix_sum = n

                not_topmost = len(prefix_sum_matrix) > 0
                not_leftmost = len(prefix_sum_row) > 0

                if not_topmost:
                    curr_prefix_sum += prefix_sum_matrix[-1][i]

                if not_leftmost:
                    curr_prefix_sum += prefix_sum_row[-1]

                if not_topmost and not_leftmost:
                    curr_prefix_sum -= prefix_sum_matrix[-1][i - 1]

                prefix_sum_row.append(curr_prefix_sum)

            prefix_sum_matrix.append(prefix_sum_row)

        prev_row = matrix[0]

        for i, row in enumerate(islice(prefix_sum_matrix, 1, len(prefix_sum_matrix)), start=1):
            curr_row = []

            for j in prev_row:
                if j == 0:
                    curr_row.append(matrix[i][j])
                else:
                    prev_square = matrix[j - 1]
                    
                    if prev_square != 0:
                        side_len = prev_square + 1



                        not_topmost = len(prefix_sum_matrix) > 0
                        not_leftmost = len(prefix_sum_row) > 0

                        if not_topmost:
                            curr_prefix_sum += prefix_sum_matrix[-1][i]

                        if not_leftmost:
                            curr_prefix_sum += prefix_sum_row[-1]

                        if not_topmost and not_leftmost:
                            curr_prefix_sum -= prefix_sum_matrix[-1][i - 1]'''