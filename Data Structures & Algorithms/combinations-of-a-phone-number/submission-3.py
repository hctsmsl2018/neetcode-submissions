DIGITS_TO_LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def _find_combinations_until_index(self, index):
        curr_digit_letters = DIGITS_TO_LETTERS[self._digits[index]] # def

        if index == 0:
            return [[c] for c in curr_digit_letters]

        prev_combinations = self._find_combinations_until_index(index - 1) # [[a], [b], [c]]

        return [[*combination, letter] for combination in prev_combinations for letter in curr_digit_letters] # [[a, d], [b, d], [c, d], [a, e], [b, e], [c, e], [a, f], [b, f], [c, f]]
    
    def letterCombinations(self, digits: str) -> List[str]:
        self._digits = digits

        if digits == "":
            return []
        else:
            combinations = self._find_combinations_until_index(len(digits) - 1)

            return ["".join(c) for c in combinations]