# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr_head = head
        start = None
        end = None

        while curr_head:
            trace_next = curr_head
            reversible = True

            for _ in range(k):
                if trace_next is None:
                    reversible = False
                    break

                trace_next = trace_next.next

            if reversible:
                curr_start = None
                old_end = end

                for _ in range(k):
                    if curr_start is None:
                        curr_start = curr_head
                        end = curr_head
                        curr_head = curr_head.next
                    else:
                        old_start = curr_start
                        old_head_next = curr_head.next
                        curr_start = curr_head
                        curr_start.next = old_start
                        curr_head = old_head_next

                end.next = None

                if start is None:
                    start = curr_start
                else:
                    old_end.next = curr_start
            else:
                end.next = curr_head
                return start

        return start