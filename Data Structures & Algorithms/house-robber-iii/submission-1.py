# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _max_money_at_node(self, node):
        if node is None:
            return 0, 0

        left_max_included, left_max_excluded = self._max_money_at_node(node.left) # 4, 4
        right_max_included, right_max_excluded = self._max_money_at_node(node.right) # 5, 1

        return node.val + left_max_excluded + right_max_excluded, max(left_max_included, left_max_excluded) + max(right_max_included, right_max_excluded)

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self._max_money_at_node(root))