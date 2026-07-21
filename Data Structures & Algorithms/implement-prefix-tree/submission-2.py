class Node:
    def __init__(self, c):
        self.val = c
        self.children = {}
        self.word_endpt = False

    def add_child(self, node):
        self.children.add(node)

class PrefixTree:

    def __init__(self):
        self.root = Node('\0')

    def insert(self, word: str) -> None:
        curr_root = self.root

        for i in word:
            if i not in curr_root.children:
                curr_root.children[i] = Node(i)

            curr_root = curr_root.children[i]

        curr_root.word_endpt = True

    def search(self, word: str) -> bool:
        curr_root = self.root

        for i in word:
            if i not in curr_root.children:
                return False

            curr_root = curr_root.children[i]

        return curr_root.word_endpt

    def startsWith(self, prefix: str) -> bool:
        curr_root = self.root

        for i in prefix:
            if i not in curr_root.children:
                return False

            curr_root = curr_root.children[i]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)