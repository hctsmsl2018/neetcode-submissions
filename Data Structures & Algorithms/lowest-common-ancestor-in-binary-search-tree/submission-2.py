# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_lca(self, node):
        if node is not None:
            curr_found = self.find_lca(node.left) | self.find_lca(node.right)

            if node.val == self.p.val:
                curr_found.add("p")

            if node.val == self.q.val:
                curr_found.add("q")

            if self.lca is None and len(curr_found) == 2:
                self.lca = node
            
            return curr_found

        return set()

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p = p
        self.q = q

        self.lca = None

        self.find_lca(root)
 
        return self.lca