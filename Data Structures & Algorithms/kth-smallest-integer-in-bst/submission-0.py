# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, root):
        if root != None:
            if self.in_order(root.left):
                return True

            self.val += 1

            if self.val == self.k:
                self.kth_smallest = root.val
                return True

            if self.in_order(root.right):
                return True

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.val = 0
        self.kth_smallest = 0

        self.in_order(root)

        return self.kth_smallest