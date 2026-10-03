from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks_enum_sorted = sorted(enumerate(tasks), key=lambda t: t[1][0]) # (0, (1, 2)), (1, (2, 4)), (2, (3, 2)), (3, (4, 1))
        sorted_tasks_ind = 0 # 4
        available_tasks = [] # (4, 2, 1)
        curr_time = 0 # 10
        processing_order = [] # 0, 2, 3, 1

        while sorted_tasks_ind < len(tasks):
            if len(available_tasks) == 0:
                i, (e, p) = tasks_enum_sorted[sorted_tasks_ind]
                heappush(available_tasks, (p, i))
                curr_time = e
                sorted_tasks_ind += 1

            while True:
                while sorted_tasks_ind < len(tasks) and tasks_enum_sorted[sorted_tasks_ind][1][0] <= curr_time:
                    i, (e, p) = tasks_enum_sorted[sorted_tasks_ind]
                    heappush(available_tasks, (p, i))
                    sorted_tasks_ind += 1

                if len(available_tasks) == 0:
                    break

                p, i = heappop(available_tasks)
                curr_time += p
                processing_order.append(i)

        return processing_order