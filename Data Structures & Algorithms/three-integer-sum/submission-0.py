class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_counter = Counter(nums)
        nums_unique_sorted = sorted(nums_counter)

        triplets = []

        for i, n in enumerate(nums_unique_sorted):
            if n > 0:
                break

            freq = nums_counter[n]

            del nums_counter[n]

            for j in islice(nums_unique_sorted, i + 1, None):
                remaining = -n - j

                if j > remaining:
                    break

                nums_counter[j] -= 1

                if nums_counter[remaining] > 0:
                    triplets.append([n, j, remaining])

                nums_counter[j] += 1

            if freq >= 2:
                remaining = -2 * n

                if nums_counter[remaining] > 0:
                    triplets.append([n, n, remaining])

            if freq >= 3 and n == 0:
                triplets.append([0, 0, 0])

        return triplets

        '''element_indices = defaultdict(set)

        for i, n in enumerate(nums):
            element_indices[n].add(i)

        solution_indices = []

        for i in range(len(nums) - 2):
            element_indices[nums[i]].remove(i)

            for j in range(i + 1, len(nums) - 1):
                element_indices[nums[j]].remove(j)

                remaining_addend = -nums[i] - nums[j]

                for k in element_indices[remaining_addend]:
                    solution_indices.append([i, j, k])

                element_indices[nums[j]].add(j)

            element_indices[nums[i]].add(i)

        return solution_indices'''
        '''nums_counter = Counter(nums)

        triplets = []

        for i in nums_counter:
            nums_counter[i] -= 1

            for j, j_count in nums_counter.items():
                if j_count > 0:
                    nums_counter[j] -= 1

                    if nums_counter[-nums[i] - nums[j]]

            nums_counter[i] += 1'''