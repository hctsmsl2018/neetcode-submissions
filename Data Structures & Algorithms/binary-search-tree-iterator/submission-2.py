# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._stack = [] # (7, r), (15, r), (20, r)
        curr = root

        while curr.left is not None:
            self._stack.append([curr, "l"])
            curr = curr.left

        self._stack.append([curr, "r"])

        self._ptr = curr.val # 20

    def next(self) -> int:
        while True:
            if len(self._stack) > 0:
                match (self._stack[-1][1]):
                    case "l":
                        left_node = self._stack[-1][0].left

                        if left_node is None:
                            self._stack[-1][1] = "v"
                        else:
                            self._stack.append([left_node, "l"])
                    case "v":
                        return_val = self._ptr
                        self._ptr = self._stack[-1][0].val
                        self._stack[-1][1] = "r"
                        return return_val
                    case "r":
                        right_node = self._stack[-1][0].right

                        if right_node is None:
                            while len(self._stack) > 0 and self._stack[-1][1] == "r":
                                self._stack.pop()

                            if len(self._stack) > 0 and self._stack[-1][1] in "l":
                                self._stack[-1][1] = "v"
                        else:
                            self._stack.append([right_node, "l"])
            else:
                return_val = self._ptr
                self._ptr = None
                return return_val

    def hasNext(self) -> bool:
        return self._ptr is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()