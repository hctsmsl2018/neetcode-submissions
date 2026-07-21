class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        if len(s1) > len(s2):
            longer = s1
            shorter = s2
        else:
            longer = s2
            shorter = s1

        prev = [True]
        still_equal = True

        for shorter_char, s3_char in zip(shorter, s3):
            if shorter_char != s3_char:
                still_equal = False

            prev.append(still_equal)

        '''
          dbbca
         100000
        a100000
        a111110
        b011010
        c001111
        c000101
        '''

        for i, longer_char in enumerate(longer): # 0-4
            curr = []

            all_false = True

            for j, prev_interleaves in enumerate(prev): # 0-5
                new_char = s3[i + j]

                add_from_longer = prev_interleaves and longer[i] == new_char
                j_prev = j - 1
                add_from_shorter = j != 0 and shorter[j_prev] == new_char and curr[j_prev]

                forms_interleaving = add_from_longer or add_from_shorter

                if forms_interleaving:
                    all_false = False

                curr.append(forms_interleaving)

            if all_false:
                return False

            prev = curr

        return prev[-1]