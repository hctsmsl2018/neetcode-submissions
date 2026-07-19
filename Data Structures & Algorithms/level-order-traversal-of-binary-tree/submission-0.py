# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        output = []
        
        queue = deque(((root, 0),))

        level = 0
        curr_level_values = []

        while len(queue) > 0:
            node, curr_level = queue.popleft()

            if level != curr_level:
                level = curr_level
                output.append(curr_level_values)
                curr_level_values = []

            curr_level_values.append(node.val)

            next_level = curr_level + 1

            if node.left is not None:
                queue.append((node.left, next_level))

            if node.right is not None:
                queue.append((node.right, next_level))

        output.append(curr_level_values)

        return output