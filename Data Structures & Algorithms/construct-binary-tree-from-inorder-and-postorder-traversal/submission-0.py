# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _create_tree_at_subnode(self, inorder_start, inorder_end, postorder_start, postorder_end): # 0, 0, 0, 0
        if inorder_start > inorder_end:
            return None

        node_val = self._postorder[postorder_end] # 3
        node_inorder_ind = self._inorder_element_to_index[node_val] # 1
        postorder_right_start_ind = postorder_start + node_inorder_ind - inorder_start # 1

        node = TreeNode(node_val)
        self._nodes_stack.append(node)

        left = self._create_tree_at_subnode(inorder_start, node_inorder_ind - 1, postorder_start, postorder_right_start_ind - 1)
        node.left = left

        right = self._create_tree_at_subnode(node_inorder_ind + 1, inorder_end, postorder_right_start_ind, postorder_end - 1)
        node.right = right

        return node
    
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        self._postorder = postorder
        self._inorder_element_to_index = {n: i for i, n in enumerate(inorder)} # 9: 0, 3: 1, 15: 2, 20: 3, 7: 4
        self._nodes_stack = [] # 3, 9

        final_ind = len(inorder) - 1

        return self._create_tree_at_subnode(0, final_ind, 0, final_ind)