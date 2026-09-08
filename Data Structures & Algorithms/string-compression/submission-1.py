class Solution:
    def compress(self, chars: List[str]) -> int: # a, 2, b, 2, c, 3
        curr_index = 0 # 6

        for i, g in groupby(chars):
            count = sum(1 for _ in g)

            chars[curr_index] = i
            curr_index += 1

            if count > 1:
                for c in str(count):
                    chars[curr_index] = c
                    curr_index += 1

        return curr_index