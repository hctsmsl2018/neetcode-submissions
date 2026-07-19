from heapq import heapify, heappop, heappush

NON_WAITING_NEXT = 0
WAITING_NEXT = 1

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_queue = [-count for count in Counter(tasks).values()]
        waiting_task = []
        curr_interval = 0
        wait_until_increment = n + 1

        heapify(tasks_queue)

        while len(tasks_queue) > 0 or len(waiting_task) > 0:
            task_candidates = {}

            if len(tasks_queue) > 0:
                task_candidates[NON_WAITING_NEXT] = -tasks_queue[0]

            if len(tasks_queue) == 0 or len(waiting_task) > 0 and waiting_task[0][0] == curr_interval:
                task_candidates[WAITING_NEXT] = waiting_task[0][1]

            best_max_source = max(task_candidates, key=lambda x: task_candidates[x])
            count = task_candidates[best_max_source]

            if best_max_source == NON_WAITING_NEXT:
                heappop(tasks_queue)

                if WAITING_NEXT in task_candidates:
                    _, waiting_count = heappop(waiting_task)
                    heappush(tasks_queue, -waiting_count)
            else:
                earliest_next_performance, _ = heappop(waiting_task)
                curr_interval = earliest_next_performance

            if count > 1:
                heappush(waiting_task, (curr_interval + wait_until_increment, count - 1))

            curr_interval += 1

        return curr_interval
        '''task_freqs = Counter(tasks).values()
        gap_including_task = n + 1

        if gap_including_task >= len(task_freqs):
            mod_assignments = task_freqs
        else:
            mod_assignments = [0] * gap_including_task
            task_freqs_sorted = sorted(task_freqs, reverse=True)

            for freq in task_freqs_sorted:
                lowest_mod_assignment = heappop(mod_assignments)
                heappush(mod_assignments, freq + lowest_mod_assignment)
        print(mod_assignments)
        highest_frequency = 0
        highest_frequency_count = 0 

        for freq in mod_assignments:
            if freq > highest_frequency:
                highest_frequency = freq
                highest_frequency_count = 1
            elif freq == highest_frequency:
                highest_frequency_count += 1

        return gap_including_task * (highest_frequency - 1) + highest_frequency_count'''