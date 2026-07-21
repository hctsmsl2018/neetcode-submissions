from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network_graph = defaultdict(set)

        for u, v, w in times:
            network_graph[u].add((v, w)) # {1: {(2, 1), (3, 2)}, 2: {(3, 2)}}

        next_edge_traversal = [(0, k)] # 
        visited_nodes = set() # 1, 2, 3
        best_travel_time = 0 # 2

        while len(next_edge_traversal) != 0:
            time, node = heappop(next_edge_traversal) # 3, 3

            if node not in visited_nodes:
                visited_nodes.add(node)
                best_travel_time = time

                for v, w in network_graph[node]:
                    heappush(next_edge_traversal, (time + w, v))

        if len(visited_nodes) == n:
            return best_travel_time
        else:
            return -1