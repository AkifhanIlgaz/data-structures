class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            current = current[letter]

        return self.search_level(current, prefix, words)

    def search_level(self, current, current_prefix, words):
        if self.end_symbol in current:
            words.append(current_prefix)

        for key in sorted(current.keys()):
            if key != self.end_symbol:
                self.search_level(current[key], current_prefix + key, words)
        return words

    def find_matches(self, document):
        matching_words = set()

        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    level = self.root
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matching_words.add(document[i:j+1])
        return matching_words
