# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def add_to_parts_list(self, parts_list, node):
        if node:
            parts_list.append(str(node.val))

            if node.left is not None or node.right is not None:
                parts_list.append("{")
                self.add_to_parts_list(parts_list, node.left)
                parts_list.append("|")
                self.add_to_parts_list(parts_list, node.right)
                parts_list.append("}")

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        parts_list = []

        self.add_to_parts_list(parts_list, root)

        return "".join(parts_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        if data.isdigit():
            return TreeNode(int(data))

        node_stack = []
        negative = False
        curr_num = None

        for i, c in enumerate(data):
            if c == "-":
                negative = True
            elif c.isdigit():
                if curr_num is None:
                    curr_num = int(c)
                else:
                    curr_num = curr_num * 10 + int(c)
            elif curr_num is not None:
                if negative:
                    curr_num *= -1

                node_stack.append(TreeNode(curr_num))
                negative = False
                curr_num = None

            prev_ind = i - 1

            if c == "|" and data[prev_ind] != "{":
                node = node_stack.pop()
                node_stack[-1].left = node
            elif c == "}" and data[prev_ind] != "|":
                node = node_stack.pop()
                node_stack[-1].right = node

        return node_stack[-1]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))