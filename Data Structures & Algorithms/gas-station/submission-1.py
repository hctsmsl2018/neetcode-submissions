from math import inf

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        balance_changes = []
        balance_from_start = []

        for g, c in zip(gas, cost):
            balance_change = g - c

            balance_changes.append(balance_change)

            if len(balance_from_start) == 0:
                balance_from_start.append(balance_change)
            else:
                balance_from_start.append(balance_from_start[-1] + balance_change)

        min_value = inf
        min_ind = None

        for i, b in enumerate(balance_from_start):
            if b < min_value:
                min_value = b
                min_ind = i

        start_ind = (min_ind + 1) % len(gas)
        curr_balance = 0

        for i in range(start_ind, start_ind + len(gas)):
            curr_balance += balance_changes[i % len(gas)]

            if curr_balance < 0:
                return -1

        return start_ind