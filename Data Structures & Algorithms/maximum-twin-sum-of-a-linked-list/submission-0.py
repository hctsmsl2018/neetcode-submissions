# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0

        curr = head

        while curr is not None:
            length += 1
            curr = curr.next

        half_length = length // 2

        curr = head
        first_half_list = [] # 5, 4
        max_twin_sum = 0 # 6

        for _ in range(half_length):
            first_half_list.append(curr.val)
            curr = curr.next

        for i in range(half_length):
            max_twin_sum = max(first_half_list[-1 - i] + curr.val, max_twin_sum)
            curr = curr.next

        return max_twin_sum