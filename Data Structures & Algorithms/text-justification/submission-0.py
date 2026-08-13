class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line_words = []
        line_words_tot_sum = 0

        for w in words:
            if len(w) + line_words_tot_sum + len(line_words) <= maxWidth:
                line_words.append(w)
                line_words_tot_sum += len(w)
            else:
                spaces = maxWidth - line_words_tot_sum
                num_spaces = len(line_words) - 1

                if num_spaces == 0:
                    lines.append(f"{line_words[0]:<{maxWidth}}")
                else:
                    shorter_space_len = spaces // num_spaces
                    shorter_space = " " * shorter_space_len
                    longer_space = " " * (shorter_space_len + 1)
                    num_longer_spaces = spaces % num_spaces

                    str_parts = []

                    for i, lw in enumerate(line_words):
                        if 0 < i <= num_longer_spaces:
                            str_parts.append(longer_space)
                        elif num_longer_spaces < i:
                            str_parts.append(shorter_space)

                        str_parts.append(lw)

                    lines.append("".join(str_parts))

                line_words = [w]
                line_words_tot_sum = len(w)

        lines.append(f"{' '.join(line_words):<{maxWidth}}")

        return lines