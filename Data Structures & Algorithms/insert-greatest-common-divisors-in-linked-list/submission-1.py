from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 18,6,6,2,10,1,3
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = head # 3
        next_node = head.next # N

        while next_node is not None:
            gcd_node = ListNode(gcd(prev_node.val, next_node.val), next_node)
            prev_node.next = gcd_node
            prev_node = next_node
            next_node = next_node.next

        return head