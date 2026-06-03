from typing import List
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree = {}

        # Initialize all characters
        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch] = set()
                    indegree[ch] = 0

        # Build constraints from adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # Topological sort
        q = deque([ch for ch in indegree if indegree[ch] == 0])
        res = []

        while q:
            ch = q.popleft()
            res.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indegree) else ""