class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = [0] # 1, 0, 8, 8 (8991)

        for i, digit_1 in enumerate(reversed(num1)): # 1, 9
            for j, digit_2 in enumerate(reversed(num2)): # 0, 9
                if digit_1 == "0" or digit_2 == "0":
                    continue

                curr_index = i + j # 1
                digits_prod = str(int(digit_1) * int(digit_2)) # 81

                regroup = False

                for prod_digit in reversed(digits_prod):
                    digits_sum = int(prod_digit) + int(regroup)

                    if curr_index < len(total):
                        digits_sum += total[curr_index]

                    regroup = digits_sum >= 10
                    ones = digits_sum % 10

                    if curr_index >= len(total):
                        while curr_index > len(total):
                            total.append(0)

                        total.append(ones)
                    else:
                        total[curr_index] = ones

                    curr_index += 1

                while regroup:
                    if regroup:
                        if curr_index == len(total):
                            total.append(1)
                            break
                        else:
                            digits_sum = total[curr_index] + 1
                            regroup = digits_sum >= 10
                            ones = digits_sum % 10
                            total[curr_index] = ones
                            curr_index += 1

        return "".join(map(str, total))[::-1]