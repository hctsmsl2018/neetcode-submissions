class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd_palindromes = [(i, i) for i in range(len(s))]
        even_palindromes = [(i, nxt) for i in range(len(s) - 1) if s[i] == s[nxt := i + 1]]

        for i in range(3, len(s) + 1):
            palindromes = odd_palindromes if i % 2 else even_palindromes
            other_palindromes = even_palindromes if i % 2 else odd_palindromes

            if palindromes != []:
                new_palindromes = [(prv, nxt) for j, k in palindromes if (prv := j - 1) != -1 and (nxt := k + 1) != len(s) and s[prv] == s[nxt]]
            else:
                new_palindromes = []

            if other_palindromes == [] and new_palindromes == []:
                return s[palindromes[0][0]: palindromes[0][1] + 1]

            palindromes[:] = new_palindromes

        longer_palindromes = even_palindromes if len(s) % 2 == 0 else odd_palindromes
        shorter_palindromes = even_palindromes if len(s) % 2 == 1 else odd_palindromes
        print(longer_palindromes, shorter_palindromes)
        if longer_palindromes != []:
            return s[longer_palindromes[0][0]: longer_palindromes[0][1] + 1]
        else:
            return s[shorter_palindromes[0][0]: shorter_palindromes[0][1] + 1]