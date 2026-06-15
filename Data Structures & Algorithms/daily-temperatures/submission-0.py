class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = [0] * len(temperatures)

        stack = []

        for i, t in reversed(tuple(enumerate(temperatures))):
            while len(stack) > 0 and stack[-1][0] <= t:
                t_old, i_old = stack.pop()

                if len(stack) > 0:
                    wait_days[i_old] = stack[-1][1] - i_old

            stack.append((t, i))
        
        while len(stack) > 0:
            t_old, i_old = stack.pop()

            if len(stack) > 0:
                wait_days[i_old] = stack[-1][1] - i_old

        return wait_days