class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev_finish_time = 0 # 21
        waiting_time_sum = 0 # 13

        for a, t in customers:
            prev_finish_time = max(prev_finish_time, a) + t
            waiting_time_sum += prev_finish_time - a

        return waiting_time_sum / len(customers)