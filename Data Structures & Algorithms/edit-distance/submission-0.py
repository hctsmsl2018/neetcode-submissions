class Solution:
    def minDistance(self, x: str, y: str) -> int:
        prev = range(len(y) + 1)
        curr = []

        for i, word_x in enumerate(x, start=1):
            curr.append(i)

            for i, word_y in enumerate(y):
                curr.append(min(curr[-1] + 1, prev[i] + (word_x != word_y), prev[i + 1] + 1))
            
            prev, curr = curr, []

        return prev[-1]