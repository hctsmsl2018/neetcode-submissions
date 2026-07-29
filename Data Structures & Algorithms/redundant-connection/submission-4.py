class Solution:
    def _search_node(self, curr_node, graph, path_list, path_set):
        print(path_list, path_set)
        for node in graph[curr_node]:
            if node not in path_set:
                path_list.append(node)
                path_set.add(node)

                cycle_start = self._search_node(node, graph, path_list, path_set)

                if cycle_start is not None:
                    return cycle_start

                path_list.pop()
                path_set.remove(node)
            elif len(path_list) >= 2 and node != path_list[-2]:
                return node

        return None
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        nodes_in_path_list = [1]
        nodes_in_path_set = {1}

        cycle_start = self._search_node(1, graph, nodes_in_path_list, nodes_in_path_set)

        cycle_edges = set()

        cycle_started = False
        cycle_start_ind = 0
        
        for i in range(len(nodes_in_path_list) - 1):
            if cycle_start == nodes_in_path_list[i] or cycle_started:
                if not cycle_started:
                    cycle_start_ind = i

                cycle_started = True
                cycle_edges.add((nodes_in_path_list[i], nodes_in_path_list[i + 1]))

        cycle_edges.add((nodes_in_path_list[-1], nodes_in_path_list[cycle_start_ind]))
        
        for a, b in edges:
            edge_removed = False

            if (a, b) in cycle_edges:
                edge_removed = True
                cycle_edges.remove((a, b))

            if (b, a) in cycle_edges:
                edge_removed = True
                cycle_edges.remove((b, a))

            if edge_removed and len(cycle_edges) == 0:
                return [a, b]