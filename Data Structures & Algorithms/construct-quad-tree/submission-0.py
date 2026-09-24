"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def inner(self, start_row, end_row, start_col, end_col):
        if start_row + 1 == end_row:
            return Node(self.grid[start_row][start_col], True, None, None, None, None)

        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2

        top_left = self.inner(start_row, mid_row, start_col, mid_col)
        top_right = self.inner(start_row, mid_row, mid_col, end_col)
        bottom_left = self.inner(mid_row, end_row, start_col, mid_col)
        bottom_right = self.inner(mid_row, end_row, mid_col, end_col)

        quadrants = (top_left, top_right, bottom_left, bottom_right)

        if all(map(lambda x: x.isLeaf, quadrants)) and len(set(map(lambda x: x.val, quadrants))) == 1:
            return Node(top_left.val, True, None, None, None, None)
        else:
            return Node(False, False, *quadrants)

    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid

        return self.inner(0, len(grid), 0, len(grid))