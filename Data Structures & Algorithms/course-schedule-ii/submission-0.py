class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list) # 0: {1, 2}, 1: {3}, 2: {3}
        indegrees = Counter() # 1: 0, 2: 0, 3: 0

        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        queue = [i for i in range(numCourses) if i not in indegrees] #
        topological_sort = [] # 0, 2, 1, 3

        while len(queue) != 0:
            course = queue.pop()
            topological_sort.append(course)

            for other_course in graph[course]:
                indegrees[other_course] -= 1

                if indegrees[other_course] == 0:
                    queue.append(other_course)

        if numCourses == len(topological_sort):
            return topological_sort
        else:
            return []