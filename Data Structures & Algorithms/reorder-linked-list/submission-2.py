# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr_count_node = head
        num_nodes = 0

        while curr_count_node is not None:
            num_nodes += 1
            curr_count_node = curr_count_node.next

        if num_nodes == 1:
            return

        half_len = num_nodes // 2

        first_half = head

        curr_split_node = head

        for i in range(half_len - 1):
            curr_split_node = curr_split_node.next

        first_half_last = curr_split_node
        curr_split_node = curr_split_node.next
        first_half_last.next = None

        odd_length = num_nodes % 2 == 1

        if odd_length:
            middle_node = curr_split_node
            curr_split_node = curr_split_node.next
            middle_node.next = None

        second_half_reversed = None

        while curr_split_node is not None:
            next_start_node = curr_split_node
            curr_split_node = curr_split_node.next
            next_start_node.next = second_half_reversed
            second_half_reversed = next_start_node

        last_node = None

        for _ in range(half_len):
            first_half_curr = first_half
            second_half_curr = second_half_reversed

            first_half = first_half.next
            second_half_reversed = second_half_reversed.next

            if last_node is not None:
                last_node.next = first_half_curr

            first_half_curr.next = second_half_curr
            last_node = second_half_curr

        if odd_length:
            last_node.next = middle_node