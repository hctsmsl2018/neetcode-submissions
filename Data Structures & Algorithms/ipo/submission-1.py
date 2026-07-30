from heapq import heappush_max, heappop_max

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits_by_capital = defaultdict(list)

        for p, c in zip(profits, capital):
            profits_by_capital[c].append(p)

        profits_by_decreasing_capital = sorted(profits_by_capital.items(), reverse=True)
        profits_queue = []

        for _ in range(k):
            while len(profits_by_decreasing_capital) > 0 and profits_by_decreasing_capital[-1][0] <= w:
                _, profits = profits_by_decreasing_capital.pop()

                for p in profits:
                    heappush_max(profits_queue, p)

            if len(profits_queue) == 0:
                return w
            else:
                w += heappop_max(profits_queue)

        return w