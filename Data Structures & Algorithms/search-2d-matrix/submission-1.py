from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tot_elements = len(matrix) * len(matrix[0])
        id_to_element = lambda x: matrix[x // len(matrix[0])][x % len(matrix[0])]

        element_id = bisect_left(range(tot_elements), target, key=id_to_element)

        return tot_elements != element_id and id_to_element(element_id) == target