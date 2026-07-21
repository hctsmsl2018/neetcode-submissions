class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o_cells = set()

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    o_cells.add((i, j))

        max_row_ind = len(board) - 1
        max_col_ind = len(board[0]) - 1
        
        while o_cells:
            curr_cells = []
            frontier = [o_cells.pop()]
            surrounded = True

            while frontier:
                next_frontier = []

                for cell in frontier:
                    curr_cells.append(cell)

                    i, j = cell

                    if i in [0, max_row_ind] or j in [0, max_col_ind]:
                        surrounded = False

                    for adj_cell in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if adj_cell in o_cells:
                            o_cells.remove(adj_cell)
                            next_frontier.append(adj_cell)

                curr_cells.extend(frontier)
                frontier = next_frontier

            if surrounded:
                for i, j in curr_cells:
                    board[i][j] = 'X'