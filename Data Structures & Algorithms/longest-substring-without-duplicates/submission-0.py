class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        repeating_characters = set()

        right = 0

        for left in range(len(s)):
            if left != 0:
                repeating_characters.remove(s[left - 1])

            while right < len(s) and s[right] not in repeating_characters:
                repeating_characters.add(s[right])
                right += 1

            curr_longest_substring = right - left
            longest_substring = max(longest_substring, curr_longest_substring)

            if right == len(s):
                break

        return longest_substring