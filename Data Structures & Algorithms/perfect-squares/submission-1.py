from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        addable_squares = tuple(i ** 2 for i in range(1, int(sqrt(n)) + 1))
        squares = [0]
        visited_squares = set()
        num_squares = 1

        while True:
            next_squares = []

            for i in squares:
                for j in addable_squares:
                    curr_sum = i + j

                    if curr_sum == n:
                        return num_squares
                    elif curr_sum not in visited_squares and curr_sum < n:
                        next_squares.append(curr_sum)
                        visited_squares.add(curr_sum)
            
            squares = next_squares
            num_squares += 1
