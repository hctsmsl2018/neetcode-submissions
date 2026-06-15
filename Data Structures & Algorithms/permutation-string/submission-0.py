class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        diff = Counter(s1)

        for c in islice(s2, len(s1)):
            diff[c] -= 1

            if diff[c] == 0:
                del diff[c]

        if len(diff) == 0:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            prev_char = s2[i - 1]

            diff[prev_char] += 1

            if diff[prev_char] == 0:
                del diff[prev_char]

            new_char = s2[i + len(s1) - 1]

            diff[new_char] -= 1

            if diff[new_char] == 0:
                del diff[new_char]

            if len(diff) == 0:
                return True

        return False
        '''s1_counter = Counter(s1)

        for c in s2:
            if c in s1:
                s1_counter[c] -= 1

            if s1_counter[c] == 0:
                del s1_counter[c]

        return len(s1_counter) == 0'''