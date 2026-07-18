"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr_nodes = {}

        list_copy = None
        last_element = None
        
        while head is not None:
            if head.random is None:
                random_node_copy = None
            else:
                random_node = head.random

                if random_node in curr_nodes:
                    random_node_copy = curr_nodes[random_node]
                else:
                    random_node_copy = Node(random_node.val)
                    curr_nodes[random_node] = random_node_copy

            if head in curr_nodes:
                curr_node_copy = curr_nodes[head]
            else:
                curr_node_copy = Node(head.val)
                curr_nodes[head] = curr_node_copy

            curr_node_copy.random = random_node_copy

            if last_element is None:
                list_copy = curr_node_copy
                last_element = curr_node_copy
            else:
                last_element.next = curr_node_copy
                last_element = curr_node_copy
            
            head = head.next

        return list_copy