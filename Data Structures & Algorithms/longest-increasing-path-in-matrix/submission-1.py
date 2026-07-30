NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def _find_longest_increasing_path_from_coordinate(self, i, j):
        longest_adjacent_increasing_path = 0

        for i_offset, j_offset in NEIGHBORS:
            i_offsetted = i + i_offset
            j_offsetted = j + j_offset

            if 0 <= i_offsetted < len(self._matrix) and 0 <= j_offsetted < len(self._matrix[0]) and self._matrix[i_offsetted][j_offsetted] > self._matrix[i][j]:
                path_len = self._lengths[i_offsetted][j_offsetted] if self._lengths[i_offsetted][j_offsetted] != 0 else self._find_longest_increasing_path_from_coordinate(i_offsetted, j_offsetted)

                longest_adjacent_increasing_path = max(longest_adjacent_increasing_path, path_len)

        self._lengths[i][j] = longest_adjacent_increasing_path + 1

        self._max_increasing_path_len = max(self._max_increasing_path_len, self._lengths[i][j])

        return self._lengths[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self._matrix = matrix
        self._lengths = [[0] * len(matrix[0]) for _ in matrix]
        self._max_increasing_path_len = 0

        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if self._lengths[i][j] == 0:
                    self._find_longest_increasing_path_from_coordinate(i, j)

        return self._max_increasing_path_len