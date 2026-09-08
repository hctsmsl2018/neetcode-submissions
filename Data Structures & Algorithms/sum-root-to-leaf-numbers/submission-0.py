# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum_subtree(self, root):
        if root is None:
            return False
        else:
            self.path_num = self.path_num * 10 + root.val

            left_not_leaf = self.sum_subtree(root.left)
            right_not_leaf = self.sum_subtree(root.right)

            if not (left_not_leaf or right_not_leaf):
                self.total_sum += self.path_num

            self.path_num //= 10

            return True

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.path_num = 0
        self.total_sum = 0

        self.sum_subtree(root)

        return self.total_sum
