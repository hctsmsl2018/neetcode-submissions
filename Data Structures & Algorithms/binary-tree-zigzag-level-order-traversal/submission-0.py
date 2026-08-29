# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        zigzag_traversal = []
        queue = deque(((0, root),))
        level = 0
        curr_row = []

        while len(queue) > 0:
            curr_level, node = queue.popleft()

            next_level = curr_level + 1

            if node.left is not None:
                queue.append((next_level, node.left))

            if node.right is not None:
                queue.append((next_level, node.right))

            if curr_level != level:
                level = curr_level
                
                if len(zigzag_traversal) % 2 == 1:
                    curr_row = curr_row[::-1]

                zigzag_traversal.append(curr_row)
                curr_row = []

            curr_row.append(node.val)

        if len(zigzag_traversal) % 2 == 1:
            curr_row = curr_row[::-1]

        zigzag_traversal.append(curr_row)

        return zigzag_traversal