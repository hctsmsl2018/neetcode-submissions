# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_with_ind(self, p_start, p_end, i_start, i_end):
        if p_start == p_end:
            return None

        root_val = self.preorder[p_start]

        inorder_root_loc = self.inorder.index(root_val, i_start, i_end)
        root_inorder_ind = i_end - inorder_root_loc - 1
        left_nodes = i_end - root_inorder_ind
        preorder_right_start = p_end - root_inorder_ind

        left = self.build_with_ind(p_start + 1, preorder_right_start, i_start, inorder_root_loc)
        right = self.build_with_ind(preorder_right_start, p_end, inorder_root_loc + 1, i_end)

        return TreeNode(root_val, left, right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder

        return self.build_with_ind(0, len(preorder), 0, len(inorder))