class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern_tokens = []

        for i, c in enumerate(p):
            if c != "*":
                next_ind = i + 1

                if next_ind < len(p) and p[next_ind] == '*':
                    pattern_tokens.append(f"{c}*")
                else:
                    pattern_tokens.append(c)

        prev_row = []

        for i in pattern_tokens:
            prev_row.append((len(prev_row) == 0 or prev_row[-1]) and len(i) == 2)

        for i in range(len(s)):
            curr_row = []

            for j in range(len(pattern_tokens)):
                if len(pattern_tokens[j]) == 2:
                    matches = (i == 0 and j == 0 or prev_row[j]) and (pattern_tokens[j][0] in {".", s[i]})
                    
                    if j > 0:
                        matches |= curr_row[-1]
                else:
                    matches = (True if i == 0 and j == 0 else j > 0 and prev_row[j - 1]) and pattern_tokens[j][0] in {".", s[i]}

                curr_row.append(matches)

            prev_row = curr_row

        return prev_row[-1]