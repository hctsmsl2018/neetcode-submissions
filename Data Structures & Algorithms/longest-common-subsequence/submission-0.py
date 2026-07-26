class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            table_i = i + 1

            for j in range(len(text2)):
                table_j = j + 1

                if text1[i] == text2[j]:
                    table[table_i][table_j] = 1 + table[i][j]
                else:
                    table[table_i][table_j] = max((table[i][table_j], table[table_i][j]))

        return table[-1][-1]