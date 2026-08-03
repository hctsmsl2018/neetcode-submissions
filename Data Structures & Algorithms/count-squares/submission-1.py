# 3: {10, 2}, 11: {2}

class CountSquares:

    def __init__(self):
        self._points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self._points[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point

        counter = 0

        for curr_y in self._points[x]:
            if y != curr_y:
                side_len = abs(y - curr_y)

                left_x = x - side_len

                if y in self._points[left_x] and curr_y in self._points[left_x]:
                    counter += self._points[x][curr_y] * self._points[left_x][y] * self._points[left_x][curr_y]

                right_x = x + side_len

                if y in self._points[right_x] and curr_y in self._points[right_x]:
                    counter += self._points[x][curr_y] * self._points[right_x][y] * self._points[right_x][curr_y]

        return counter

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)