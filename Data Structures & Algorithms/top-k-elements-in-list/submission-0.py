from random import randint

class Solution:
    def quickselect(self, start, end, k):
        pivot_element = self.elements_and_freqs[randint(start, end)]

        pivot_ind = start
        
        for i, element in islice(enumerate(self.elements_and_freqs), start, end + 1):
            if element < pivot_element:
                pivot_ind += 1
            elif element == pivot_element:
                pivot_original_ind = i

        self.elements_and_freqs[pivot_ind], self.elements_and_freqs[pivot_original_ind] = self.elements_and_freqs[pivot_original_ind], self.elements_and_freqs[pivot_ind]

        left = start
        right = end

        while left < right:
            while self.elements_and_freqs[left] < pivot_element:
                left += 1

            while self.elements_and_freqs[right] > pivot_element:
                right -= 1

            self.elements_and_freqs[left], self.elements_and_freqs[right] = self.elements_and_freqs[right], self.elements_and_freqs[left]

        expected_ind = end - k + 1

        if pivot_ind > expected_ind:
            self.quickselect(start, pivot_ind - 1, k - end + pivot_ind - 1)
        elif pivot_ind < expected_ind:
            self.quickselect(pivot_ind + 1, end, k)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.elements_and_freqs = [(freq, i) for i, freq in Counter(nums).items()]

        self.quickselect(0, len(self.elements_and_freqs) - 1, k)
        
        return [i for _, i in self.elements_and_freqs[-k:]]