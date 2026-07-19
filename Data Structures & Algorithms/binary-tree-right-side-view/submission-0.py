# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = deque(((root, 1),))
        rightmost_values = []
        level = 1
        curr_val = None

        while len(queue) > 0:
            node, curr_level = queue.popleft()

            if level != curr_level:
                rightmost_values.append(curr_val)

            next_level = curr_level + 1

            if node.left is not None:
                queue.append((node.left, next_level))

            if node.right is not None:
                queue.append((node.right, next_level))

            level = curr_level
            curr_val = node.val

        rightmost_values.append(curr_val)

        return rightmost_values