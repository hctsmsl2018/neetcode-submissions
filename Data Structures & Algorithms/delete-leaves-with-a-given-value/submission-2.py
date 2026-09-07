# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _remove_leaves_at_node(self, node, parent, side):
        if node is not None:
            self._remove_leaves_at_node(node.left, node, "left")
            self._remove_leaves_at_node(node.right, node, "right")

            if self._target == node.val and node.left is None and node.right is None:
                if parent is None:
                    self._root_removed = True
                else:
                    setattr(parent, side, None)

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self._target = target
        self._root_removed = False

        self._remove_leaves_at_node(root, None, None)

        if self._root_removed:
            return None
        else:
            return root