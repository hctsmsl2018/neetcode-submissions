class Solution:
    # index=0 recursive calls: [a], [aa]
    # index=1 recursive calls: [a, a]
    # index=2 recursive calls: [aa, b], [a, a, b]
    def _get_partition_from_index(self, index):
        if index == len(self._s):
            self._palindrome_partitions.append(self._current_partition.copy())

        curr_substr_chars = []

        for i in range(index, len(self._s)):
            curr_substr_chars.append(self._s[i])

            for j in range(len(curr_substr_chars) // 2):
                if curr_substr_chars[j] != curr_substr_chars[-j - 1]:
                    break
            else:
                self._current_partition.append("".join(curr_substr_chars))
                self._get_partition_from_index(i + 1)
                self._current_partition.pop()

    def partition(self, s: str) -> List[List[str]]:
        self._s = s
        self._current_partition = []
        self._palindrome_partitions = []

        self._get_partition_from_index(0)

        return self._palindrome_partitions