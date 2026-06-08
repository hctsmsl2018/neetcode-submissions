class Solution:
    def check_valid_subtree(self, node, parent):
        if node in self.visited:
            return False

        self.visited.add(node)

        valid_subtree = True

        for neighbor in self.tree[node]:
            if neighbor != parent:
                valid_subtree = valid_subtree and self.check_valid_subtree(neighbor, node)

        return valid_subtree

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.tree = defaultdict(list)

        for s, e in edges:
            self.tree[s].append(e)
            self.tree[e].append(s)

        self.visited = set()

        return self.check_valid_subtree(0, None) and len(self.visited) == n

