'''
1111
0111
0011
00
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr_height = amount + 1
        arr_width = len(coins) + 1

        subproblems = [[0] * arr_width for _ in range(arr_height)]
        subproblems[0][0] = 1

        for i in range(arr_height):
            for j in range(1, arr_width):
                left = j - 1

                subproblems[i][j] = subproblems[i][left]

                prev_tot_ind = i - coins[left]

                if prev_tot_ind >= 0:
                    subproblems[i][j] += subproblems[prev_tot_ind][j]

        return subproblems[-1][-1]