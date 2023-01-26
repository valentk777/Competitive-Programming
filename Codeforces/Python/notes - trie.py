# region - SEARCH

# this trie was used to create a paths for prefix permutation. This idea often used in algorithms.
# tree using matrix (faster, less memory)
class TrieArray:
    def __init__(self, m):
        self.root = [None] * m
        self.size = m

    def insert(self, _list):
        current_root = self.root

        for element in _list:
            if current_root[element] is None:
                current_root[element] = [None] * self.size

            current_root = current_root[element]

    def query(self, word):
        current_root = self.root
        prefix = []

        for element in word:
            if current_root[element] is None:
                return prefix

            current_root = current_root[element]
            prefix.append(element)

        return prefix


# this trie was used to create a paths for prefix permutation. This idea often used in algorithms.
# tree using dictionary
class TrieDict:
    def __init__(self):
        self.root = {}

    def insert(self, _list):
        current_root = self.root

        for element in _list:
            if element not in current_root:
                current_root[element] = {}

            current_root = current_root[element]

    def query(self, word):
        current_root = self.root
        prefix = []

        for element in word:
            if element not in current_root:
                return prefix

            current_root = current_root[element]
            prefix.append(element)

        return prefix

# endregion
