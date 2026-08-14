class Solution(object):
    def n_sum(self, lower):
        if len(self.curr_nums) == 3:
            last_element = self.target - self.curr_nums_sum
            if last_element <= self.nums[lower] and last_element in self.nums_set:
                self.curr_nums.append(last_element)
                self.quads.add(tuple(self.curr_nums))
                self.curr_nums.pop()
        else:
            for i in range(lower, len(self.nums) - 3 + len(self.curr_nums)):
                self.curr_nums.append(self.nums[i])
                self.curr_nums_sum += self.nums[i]

                self.n_sum(i + 1)

                self.curr_nums.pop()
                self.curr_nums_sum -= self.nums[i]

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort(reverse=True)
        self.nums = nums
        self.nums_set = set(nums)
        self.target = target
        self.curr_nums = []
        self.curr_nums_sum = 0
        self.quads = set()

        self.n_sum(0)

        return list(map(list, self.quads))
        