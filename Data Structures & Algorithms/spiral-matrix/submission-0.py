class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_order = []

        min_row = 0
        max_row = len(matrix) - 1

        min_col = 0
        max_col = len(matrix[0]) - 1

        i = 0
        j = 0
        direction = "d" if max_col == 0 else "r"

        total_cells = len(matrix) * len(matrix[0])

        while len(spiral_order) < total_cells:
            print(i, j)
            spiral_order.append(matrix[i][j])

            match (direction):
                case "u":
                    i -= 1
                
                    if i == min_row:
                        direction = "r"
                        min_col += 1
                case "d":
                    i += 1
                
                    if i == max_row:
                        direction = "l"
                        max_col -= 1
                case "r":
                    j += 1
                
                    if j == max_col:
                        direction = "d"
                        min_row += 1
                case "l":
                    j -= 1
                
                    if j == min_col:
                        direction = "u"
                        max_row -= 1

        return spiral_order