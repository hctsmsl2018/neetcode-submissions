class Solution:
    def myPow(self, x: float, n: int) -> float:
        if -1 <= n <= 1:
            return x ** n

        return self.myPow(x, n // 2) ** 2 * (x ** (n % 2))