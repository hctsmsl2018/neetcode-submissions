from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_node_max_path(self, node):
        if node is None:
            return 0
        else:
            left_sum = self.find_node_max_path(node.left)
            right_sum = self.find_node_max_path(node.right)

            best_sum_to_root = node.val + max(0, left_sum, right_sum)

            self.max_path_sum = max(self.max_path_sum, best_sum_to_root, node.val + left_sum + right_sum)

            return best_sum_to_root

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -inf

        self.find_node_max_path(root)

        return self.max_path_sum