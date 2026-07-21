"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        val_to_node = {node.val: Node(node.val)}

        visited = {node.val}
        frontier = {node.val: node}

        while len(frontier) > 0:
            new_frontier = {}

            for curr_node in frontier.values():
                neighbors = []

                for neighbor in curr_node.neighbors:
                    val = neighbor.val

                    if val not in visited:
                        new_frontier[val] = neighbor

                    visited.add(val)
                    neighbors.append(val)

                for val in neighbors:
                    if val not in val_to_node:
                        val_to_node[val] = Node(val)

                    val_to_node[curr_node.val].neighbors.append(val_to_node[val])

            frontier = new_frontier
            
        return val_to_node[node.val]