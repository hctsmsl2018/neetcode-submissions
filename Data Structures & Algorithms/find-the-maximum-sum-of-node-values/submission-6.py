from math import inf
import sys

class Solution:
    def _get_subtree_max_sum(self, node):
        prev_node = self._prev_node
        nodes_max_tot = 0
        xors_needed = 0
        min_diff = inf
        eq_xor = False

        for i in chain(self._graph[node], (node,)):
            if self._prev_node is None or i != self._prev_node:
                if i == node:
                    num, xor = self._nums[node], self._nums[node] ^ self._k
                else:
                    self._prev_node = node

                    num, xor = self._get_subtree_max_sum(i)

                    self._prev_node = prev_node

                if num < xor:
                    nodes_max_tot += xor
                    xors_needed += 1
                elif num > xor:
                    nodes_max_tot += num
                else:
                    eq_xor = True

                min_diff = min(min_diff, abs(num - xor))

        if eq_xor:
            num_max = nodes_max_tot
            xor_max = nodes_max_tot
        elif xors_needed % 2 == 0:
            num_max = nodes_max_tot
            xor_max = nodes_max_tot - min_diff
        else:
            num_max = nodes_max_tot - min_diff
            xor_max = nodes_max_tot

        return (num_max, xor_max)

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sys.setrecursionlimit(30000)

        self._nums = nums
        self._k = k
        self._graph = defaultdict(set)
        self._prev_node = None

        for u, v in edges:
            self._graph[u].add(v)
            self._graph[v].add(u)

        return self._get_subtree_max_sum(0)[0]