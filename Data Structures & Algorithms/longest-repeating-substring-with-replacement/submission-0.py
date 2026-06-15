class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring_len = 0

        char_counter = Counter()

        right = 0

        for left in range(len(s)):
            if left > 0:
                prev_char = s[left - 1]

                if char_counter[prev_char] == 1:
                    del char_counter[prev_char]
                else:
                    char_counter[prev_char] -= 1
            
            while right < len(s):
                char_counter[s[right]] += 1

                if right + 1 - left - max(char_counter.values(), default=0) > k:
                    if char_counter[s[right]] == 1:
                        del char_counter[s[right]]
                    else:
                        char_counter[s[right]] -= 1

                    break
                
                right += 1

            longest_substring_len = max(right - left, longest_substring_len)
            
            if right == len(s):
                break

        return longest_substring_len