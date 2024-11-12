import trie # use trie data structure

class WordDictionary:

    def __init__(self):
        self.tr = trie()

    def addWord(self, word: str) -> None:
        self.tr.insert(word)

    def search(self, word: str) -> bool:
        curr = self.tr.root
        
        return NotImplementedError()
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
