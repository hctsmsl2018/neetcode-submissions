# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_node = head
        n_ahead = curr_node

        for _ in range(n):
            n_ahead = n_ahead.next

        if n_ahead == None:
            return curr_node.next

        while n_ahead.next != None:
            curr_node = curr_node.next
            n_ahead = n_ahead.next

        curr_node.next = curr_node.next.next

        return head