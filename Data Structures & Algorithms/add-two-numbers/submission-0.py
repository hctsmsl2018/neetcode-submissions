# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1.next
        curr_l2 = l2.next
        first_sum = l1.val + l2.val
        sol_start = ListNode(first_sum % 10, None)
        curr_sol = sol_start
        regroup = first_sum >= 10

        while curr_l1 or curr_l2:
            curr_dig_sum = regroup

            if curr_l1:
                curr_dig_sum += curr_l1.val
                curr_l1 = curr_l1.next

            if curr_l2:
                curr_dig_sum += curr_l2.val
                curr_l2 = curr_l2.next

            regroup = curr_dig_sum >= 10
            curr_sol.next = ListNode(curr_dig_sum % 10, None)
            curr_sol = curr_sol.next

        if regroup:
            curr_sol.next = ListNode(1, None)

        return sol_start