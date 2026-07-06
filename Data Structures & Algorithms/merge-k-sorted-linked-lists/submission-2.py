from heapq import heapify, heappop, heappush

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = None
        list_tail = None

        list_heap = [(l.val, i, l.next) for i, l in enumerate(lists) if l]
        heapify(list_heap)

        while list_heap:
            smallest, list_ind, next_node = heappop(list_heap)
              
            if sorted_list == None:
                sorted_list = ListNode(smallest, None)
                list_tail = sorted_list
            else:
                list_tail.next = ListNode(smallest, None)
                list_tail = list_tail.next

            if next_node:
                heappush(list_heap, (next_node.val, list_ind, next_node.next))

        return sorted_list