class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from_high = len(numbers) - 1

        for i, n in enumerate(numbers):
            complement = target - n

            while numbers[from_high] > complement:
                from_high -= 1

            if numbers[from_high] == complement:
                return [i + 1, from_high + 1]