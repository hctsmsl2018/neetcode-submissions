class UnionFind:
    def __init__(self):
        self.union_find = {}

    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)

        self.union_find[j_parent] = i_parent

    def find(self, i):
        parent = i

        if parent in self.union_find:
            while parent != self.union_find[parent]:
                parent = self.union_find[parent]

        self.union_find[i] = parent

        return parent

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        edges = []

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i < j:
                    edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))

        edges.sort()

        total = 0
        num_unions = 0
        max_unions = len(points) - 1

        union_find = UnionFind()

        for weight, p1, p2 in edges:
            p1_parent = union_find.find(p1)
            p2_parent = union_find.find(p2)

            if p1_parent == p2_parent:
                continue

            total += weight

            union_find.union(p1_parent, p2_parent)

            num_unions += 1

            if num_unions == max_unions:
                return total