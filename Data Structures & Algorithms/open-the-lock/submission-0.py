class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        no_revisit = set(deadends)

        if '0000' in deadends:
            return -1
        
        no_revisit.add('0000')
        queue = deque((('0000', 0), ))

        while queue:
            curr = queue.popleft()

            if curr[0] == target:
                return curr[1]

            for i, c in enumerate(curr[0]):
                int_wheel = int(c)
                nxt = (int_wheel + 1) % 10
                prev = (int_wheel - 1) % 10
                next_str = curr[0][:i] + str(nxt) + curr[0][i + 1:]
                prev_str = curr[0][:i] + str(prev) + curr[0][i + 1:]
                
                for cmb in (next_str, prev_str):
                    if cmb not in no_revisit:
                        queue.append((cmb, curr[1] + 1))

                        no_revisit.add(cmb)

        return -1