class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_row_ind = len(grid) - 1
        max_col_ind = len(grid[0]) - 1

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1

                    frontier = {(i, j)}
                    
                    while len(frontier) > 0:
                        new_frontier = set()

                        for indices in frontier:
                            curr_i, curr_j = indices

                            grid[curr_i][curr_j] = "0"

                            if curr_i > 0:
                                up_i = curr_i - 1

                                if grid[up_i][curr_j] == "1":
                                    new_frontier.add((up_i, curr_j))

                            if curr_i < max_row_ind:
                                down_i = curr_i + 1

                                if grid[down_i][curr_j] == "1":
                                    new_frontier.add((down_i, curr_j))

                            if curr_j > 0:
                                left_j = curr_j - 1

                                if grid[curr_i][left_j] == "1":
                                    new_frontier.add((curr_i, left_j))

                            if curr_j < max_col_ind:
                                right_j = curr_j + 1

                                if grid[curr_i][right_j] == "1":
                                    new_frontier.add((curr_i, right_j))

                        frontier = new_frontier

        return num_islands