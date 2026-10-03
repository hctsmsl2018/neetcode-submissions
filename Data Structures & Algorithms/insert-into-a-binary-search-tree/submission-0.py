# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            curr_node = root

            while True:
                if val < curr_node.val:
                    if curr_node.left:
                        curr_node = curr_node.left
                    else:
                        curr_node.left = TreeNode(val)
                        break
                else:
                    if curr_node.right:
                        curr_node = curr_node.right
                    else:
                        curr_node.right = TreeNode(val)
                        break

            return root
        else:
            return TreeNode(val)