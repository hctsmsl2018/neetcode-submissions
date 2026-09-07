class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        min_costs = [min(costs)] # 2, 4, 6, 7, 9, 11
        prev_7_day_interval_ind = -1 # 4
        prev_30_day_interval_ind = -1 # 

        for i in islice(days, 1, len(days)):
            min_costs_for_tickets = [min_costs[-1] + costs[0]] # 11, 16, 15

            max_7_day_interval_prev_day = i - 7 # 13

            while days[prev_7_day_interval_ind + 1] <= max_7_day_interval_prev_day:
                prev_7_day_interval_ind += 1

            costs_7_days = costs[1]

            if prev_7_day_interval_ind != -1:
                costs_7_days += min_costs[prev_7_day_interval_ind]
            
            min_costs_for_tickets.append(costs_7_days)

            max_30_day_interval_prev_day = i - 30 # -10

            while days[prev_30_day_interval_ind + 1] <= max_30_day_interval_prev_day:
                prev_30_day_interval_ind += 1

            costs_30_days = costs[2]

            if prev_30_day_interval_ind != -1:
                costs_30_days += min_costs[prev_30_day_interval_ind]
            
            min_costs_for_tickets.append(costs_30_days)

            min_costs.append(min(min_costs_for_tickets))

        return min_costs[-1]