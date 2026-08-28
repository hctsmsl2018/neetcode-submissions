class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        curr_ind = 0

        for i in s:
            if i == t[curr_ind]:
                curr_ind += 1

            if curr_ind == len(t):
                return 0

        return len(t) - curr_ind