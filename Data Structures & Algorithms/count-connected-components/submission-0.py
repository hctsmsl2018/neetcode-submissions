class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        num_components = 0
        not_visited = set(range(n))

        while len(not_visited) > 0:
            frontier = [not_visited.pop()]

            while len(frontier) > 0:
                new_frontier = []
                
                for node in frontier:
                    for neighbor in graph[node]:
                        if neighbor in not_visited:
                            not_visited.remove(neighbor)
                            new_frontier.append(neighbor)
                
                frontier = new_frontier

            num_components += 1

        return num_components