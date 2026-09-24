class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        def get_prod(k):
            if k < 2:
                return 0

            smallest_part = n // k
            number_gt_smaller = n % k
            return  (smallest_part + 1) ** number_gt_smaller * smallest_part ** (k - number_gt_smaller)

        sqrt = int(n ** 0.5)
        curr_less = sqrt - 1
        dir_less = [get_prod(sqrt), get_prod(curr_less)]
        curr_more = sqrt + 2
        dir_more = [get_prod(curr_more - 1), get_prod(curr_more)]

        if dir_less[0] >= dir_less[1] and dir_less[0] >= dir_more[0]:
            return dir_less[0]

        if dir_more[0] >= dir_more[1] and dir_more[0] >= dir_less[0]:
            return dir_more[0]
        
        less_not_at_end = curr_less > 2
        more_not_at_end = curr_more < n

        while less_not_at_end or more_not_at_end:
            if less_not_at_end:
                curr_less -= 1
                nxt_less = get_prod(curr_less)

                if dir_less[1] >= dir_less[0] and dir_less[1] >= nxt_less:
                    return dir_less[1]

                if curr_less == 2:
                    less_not_at_end = False

                dir_less = [dir_less[1], nxt_less]
                
            if more_not_at_end:
                curr_more += 1
                nxt_more = get_prod(curr_more)

                if dir_more[1] >= dir_more[0] and dir_more[1] >= nxt_more:
                    return dir_more[1]

                if curr_more == n:
                    more_not_at_end = False

                dir_more = [dir_more[1], nxt_more]

        return max(dir_more + dir_less)