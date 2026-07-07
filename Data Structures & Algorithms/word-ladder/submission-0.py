class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_graph = defaultdict(set)

        for word in {beginWord, endWord, *wordList}:
            for other_word in wordList:
                if sum(char != other_char for char, other_char in zip(word, other_word)) == 1:
                    word_graph[word].add(other_word)

        queue = deque(((beginWord, 1),))
        visited = {beginWord}

        while len(queue) != 0:
            word, seq_len = queue.popleft()

            next_seq_len = seq_len + 1

            for other_word in word_graph[word]:
                if other_word == endWord:
                    return next_seq_len
                elif other_word not in visited:
                    queue.append((other_word, next_seq_len))
                    visited.add(other_word)

        return 0