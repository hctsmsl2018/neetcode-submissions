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
        if head != None:
            length = 1

            curr_node = head

            while curr_node.next != None:
                curr_node = curr_node.next
                length += 1

            front_ptr = head
            to_insert_ptr = head

            for _ in range((length + 1) // 2 - 1):
                to_insert_ptr = to_insert_ptr.next

            prev_insert_ptr = to_insert_ptr
            to_insert_ptr = prev_insert_ptr.next
            prev_insert_ptr.next = None

            insert_ptrs = []

            while to_insert_ptr != None:
                insert_ptrs.append(to_insert_ptr)
                to_insert_ptr = to_insert_ptr.next

            while insert_ptrs != []:
                front_ptr_nxt = front_ptr.next
                to_insert_nxt = insert_ptrs.pop()
                front_ptr.next = to_insert_nxt
                to_insert_nxt.next = front_ptr_nxt
                front_ptr = front_ptr_nxt