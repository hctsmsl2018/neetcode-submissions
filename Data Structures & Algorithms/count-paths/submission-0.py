class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 1
        m_edges = m - 1
        n_edges = n - 1
        choose_from = m_edges + n_edges
        choose = min((m_edges, n_edges))

        for i in range(choose_from, choose_from - choose, -1):
            paths *= i

        for i in range(2, choose + 1):
            paths //= i

        return paths