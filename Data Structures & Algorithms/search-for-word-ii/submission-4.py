class Solution:
    def find_subtrie(self, subtrie, prev_char=None, prev_pos=None):
        for c, subsubtrie in subtrie.items():
            if c == "*":
                self.found_words.add(subsubtrie)
            elif prev_pos is None:
                if len(self.letter_to_words[c]) > 0:
                    self.find_subtrie(subsubtrie, c, self.letter_to_words[c])
            else:
                for pos in prev_pos:
                    i, j = pos

                    next_pos = []

                    if i > 0:
                        up_ind = (i - 1, j)

                        if up_ind in self.letter_to_words[c]:
                            next_pos.append(up_ind)

                    if i < self.height_ind_lim:
                        down_ind = (i + 1, j)

                        if down_ind in self.letter_to_words[c]:
                            next_pos.append(down_ind)

                    if j > 0:
                        left_ind = (i, j - 1)

                        if left_ind in self.letter_to_words[c]:
                            next_pos.append(left_ind)

                    if j < self.width_ind_lim:
                        right_ind = (i, j + 1)

                        if right_ind in self.letter_to_words[c]:
                            next_pos.append(right_ind)

                    if len(next_pos) > 0:
                        self.letter_to_words[prev_char].remove((i, j))

                        self.find_subtrie(subsubtrie, c, next_pos)

                        self.letter_to_words[prev_char].add((i, j))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board

        trie = {}

        for w in words:
            subtrie = trie

            for c in w:
                if c not in subtrie:
                    subtrie[c] = {}

                subtrie = subtrie[c]

            subtrie["*"] = w

        self.letter_to_words = defaultdict(set)

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                self.letter_to_words[c].add((i, j))

        self.height_ind_lim = len(board) - 1
        self.width_ind_lim = len(board[0]) - 1

        self.found_words = set()

        self.find_subtrie(trie)

        return list(self.found_words)