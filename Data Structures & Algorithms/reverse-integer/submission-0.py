class Solution:
    def reverse(self, x: int) -> int:
        neg_result = x < 0

        limit = 2 ** 31 if neg_result else 2 ** 31 - 1

        x_abs = abs(x)
        x_reversed = 0

        while x_abs != 0:
            x_reversed = x_reversed * 10 + x_abs % 10

            if x_reversed > limit:
                return 0

            x_abs //= 10

        return x_reversed * (-1) ** int(neg_result)