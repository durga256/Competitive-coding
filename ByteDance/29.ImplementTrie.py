from collections import defaultdict
class Trie:
    def __init__(self):
        self.trie=[]
        self.temp=defaultdict()

    def insert(self, word: str) -> None:
        self.trie.append(word)
        for i in range(len(word)):
            self.temp[word[:i+1]]=0

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.temp:
            return True
        return False