class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarr_sum = sum(islice(arr, k)) # 18
        num_subarrs = int(subarr_sum / k >= threshold) # 3

        for i in range(k, len(arr)):
            subarr_sum += arr[i] - arr[i - k]

            if subarr_sum / k >= threshold:
                num_subarrs += 1

        return num_subarrs