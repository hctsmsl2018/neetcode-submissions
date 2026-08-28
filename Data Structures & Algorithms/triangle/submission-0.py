class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        while len(triangle) > 1:
            base = triangle[-1]
            base_above = triangle[-2]
            new_base = []
            for i in range(len(base_above)):
                new_base.append(min(base[i:i + 2]) + base_above[i])
            triangle = triangle[:-2]
            triangle.append(new_base)
        return triangle[0][0]