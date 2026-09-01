# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head # None
        last_node = None # 1
        length = 0 # 1

        while curr is not None:
            last_node = curr
            curr = curr.next
            length += 1

        effective_rotate = k % length # 0

        if effective_rotate == 0:
            return head

        curr = head # 1

        for _ in range(length - effective_rotate - 1):
            curr = curr.next

        new_start = curr.next # 4
        curr.next = None
        last_node.next = head

        return new_start