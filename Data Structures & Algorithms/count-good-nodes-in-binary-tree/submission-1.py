from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _find_subtree_good_nodes(self, node, prev_max=-inf):
        if node is None:
            return 0

        next_prev_max = max(node.val, prev_max)

        return self._find_subtree_good_nodes(node.left, next_prev_max) + self._find_subtree_good_nodes(node.right, next_prev_max) + int(node.val >= prev_max)

    def goodNodes(self, root: TreeNode) -> int:
        return self._find_subtree_good_nodes(root)