import sys

class Solution:
    def dfs(self, node, prev):
        tree_sum = self.values[node]

        for i in self.edge_dict[node]:
            if i != prev:
                tree_sum += self.dfs(i, node)

        if tree_sum % self.k == 0:
            self.components += 1
            return 0
        else:
            return tree_sum


    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        sys.setrecursionlimit(40000)

        self.edge_dict = [list() for _ in range(n)]

        for a, b in edges:
            self.edge_dict[a].append(b)
            self.edge_dict[b].append(a)

        self.k = k
        self.values = values
        self.components = 0

        self.dfs(0, n)

        return self.components