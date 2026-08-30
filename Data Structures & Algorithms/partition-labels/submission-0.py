class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        str_parts = [] # (0, 8), (1, 5), (4, 7), (9, 14), (10, 15), (11, 11), (13, 13), (16, 19), (17, 22), (18, 23), (20, 20), (21, 21)
        char_indices = {} # a: 0, b: 1, c: 2, d: 3, e: 4, f: 5, g: 6, h: 7, i: 8, j: 9, k: 10, l: 11

        for i, c in enumerate(s):
            if c in char_indices:
                str_parts[char_indices[c]][1] = i
            else:
                char_indices[c] = len(str_parts)
                str_parts.append([i, i])

        interval_start = 0 # 16
        interval_end = 0 # 23
        partition_sizes = [] # 9, 7, 8

        for s, e in str_parts:
            if interval_end < s:
                partition_sizes.append(interval_end - interval_start + 1)
                interval_start = s
                interval_end = e
            else:
                interval_end = max(interval_end, e)

        partition_sizes.append(interval_end - interval_start + 1)

        return partition_sizes