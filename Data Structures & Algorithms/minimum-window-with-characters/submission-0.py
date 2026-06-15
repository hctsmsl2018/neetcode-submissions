class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_chars = set(t)
        min_length = len(s) + 1
        min_length_range = None

        char_counter = Counter(t)

        right = 0

        for left in range(len(s)):
            prev_char = s[left - 1]

            if left > 0 and prev_char in t_chars:
                char_counter[prev_char] += 1

            while right < len(s) and max(char_counter.values()) > 0:
                char_counter[s[right]] -= 1

                right += 1

            if right == len(s) and max(char_counter.values()) > 0:
                break

            window_len = right - left

            if window_len < min_length:
                min_length = window_len
                min_length_range = (left, right)

        return "" if min_length_range is None else s[slice(*min_length_range)]