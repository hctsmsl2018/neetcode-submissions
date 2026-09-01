# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _check_from_node(self, node):
        if node is not None:
            self._check_from_node(node.left)

            self._prev, self._curr, self._next = self._curr, self._next, node

            if self._curr is not None:
                if self._prev is not None:
                    if self._prev.val > self._curr.val < self._next.val or self._prev.val < self._curr.val > self._next.val:
                        self._swapped.append(self._curr)
                elif self._curr.val > self._next.val:
                    self._swapped.append(self._curr)

            self._check_from_node(node.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self._prev = None # 3
        self._curr = None # 2
        self._next = None # 4

        self._swapped = [] # 3, 2

        self._check_from_node(root)

        if self._curr.val > self._next.val:
            self._swapped.append(self._next)

        self._swapped[0].val, self._swapped[-1].val = self._swapped[-1].val, self._swapped[0].val