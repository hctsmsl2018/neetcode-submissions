class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegrees = defaultdict(int)

        for a, b in prerequisites:
            graph[a].add(b)
            indegrees[b] += 1

        visited = 0

        queue = [i for i in range(numCourses) if i not in indegrees]

        while len(queue) != 0:
            curr_node = queue.pop()

            visited += 1

            for i in graph[curr_node]:
                indegrees[i] -= 1

                if indegrees[i] == 0:
                    queue.append(i)

        return visited == numCourses