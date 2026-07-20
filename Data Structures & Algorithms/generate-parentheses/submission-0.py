class Solution:
    # 

    # (: 2
    # ): 1
    def _generate_from_curr_parentheses(self, num_opening_parentheses, num_closing_parentheses):
        if num_opening_parentheses + num_closing_parentheses == self._parentheses_str_len:
            self._generated_parentheses.append("".join(self._curr_generated_parentheses))
        else:
            if num_opening_parentheses < self._n:
                self._curr_generated_parentheses.append("(")
                self._generate_from_curr_parentheses(num_opening_parentheses + 1, num_closing_parentheses)
                self._curr_generated_parentheses.pop()

            if num_closing_parentheses < num_opening_parentheses:
                self._curr_generated_parentheses.append(")")
                self._generate_from_curr_parentheses(num_opening_parentheses, num_closing_parentheses + 1)
                self._curr_generated_parentheses.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self._n = n
        self._parentheses_str_len = 2 * n # 6
        self._curr_generated_parentheses = []
        self._generated_parentheses = [] # ((())), (()()), (())(), ()(()), ()()()

        self._generate_from_curr_parentheses(0, 0)

        return self._generated_parentheses