class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        curr_amounts = [0]
        seen_amounts = set()
        num_coins = 1

        while curr_amounts != []:
            next_amounts = []

            for i in curr_amounts:
                for j in coins:
                    curr_amount = i + j

                    if curr_amount == amount:
                        return num_coins
                    elif curr_amount not in seen_amounts and curr_amount < amount:
                        next_amounts.append(curr_amount)
                        seen_amounts.add(curr_amount)

            curr_amounts = next_amounts
            num_coins += 1

        return -1