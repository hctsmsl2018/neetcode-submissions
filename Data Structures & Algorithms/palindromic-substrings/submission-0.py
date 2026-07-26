class Solution:
    def count_substrings_from_base(self, initial_substrings, initial_length):
        prev = initial_substrings

        for length in range(initial_length, len(self.s) + 1, 2):
            curr = []

            for i in prev:
                before = i - 1
                after = i + length

                if 0 <= before and after < len(self.s) and self.s[before] == self.s[after]:
                    self.palindormic_substrings += 1
                    curr.append(before)

            if len(curr) == 0:
                break

            prev = curr

    def countSubstrings(self, s: str) -> int:
        self.s = s

        length_1_substrings = list(range(len(s)))
        length_2_substrings = [i for i in range(len(s) - 1) if s[i] == s[i + 1]]

        self.palindormic_substrings = len(length_1_substrings) + len(length_2_substrings)

        self.count_substrings_from_base(length_1_substrings, 1)
        self.count_substrings_from_base(length_2_substrings, 2)

        return self.palindormic_substrings