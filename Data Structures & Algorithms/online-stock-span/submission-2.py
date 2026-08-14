class StockSpanner:

    def __init__(self):
        self._span_history = [] # (100, 1), (85, 7)
        self._day = 1 # 8

    def next(self, price: int) -> int:
        while len(self._span_history) > 0 and self._span_history[-1][0] <= price:
            self._span_history.pop()

        self._span_history.append((price, self._day))
        self._day += 1

        if len(self._span_history) == 1:
            return self._span_history[0][1]
        else:
            return self._span_history[-1][1] - self._span_history[-2][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)