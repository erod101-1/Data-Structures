class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False # set to true when we complete word

class Trie:
    def __init__(self):
        self.root = TrieNode() # instantiate root

    def insert(self, word: str) -> None:
        curr = self.root # point to root of the tree
        for c in word: # iterate through are word
            if c not in curr.children: # branch out from not if char doesnt exist
                curr.children[c] = TrieNode()
            curr = curr.children[c] # point to latest char in tree
        curr.word = True # mark end of word


    def search(self, word: str) -> bool:
        curr = self.root 
        for c in word: 
            if c not in curr.children:
                return False
            curr = curr.children[c] # iterate down
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


def main() -> bool:
    tr = Trie()
    tr.insert('apple')
    tr.insert('apple')
        
    assert(tr.search('apple') == True)
    assert(tr.search('app') == False)
    assert(tr.startsWith('app') == True)
    tr.insert('ape')
    assert(tr.search('ap') == False)
    assert(tr.search('ape') == True)
    
    return True

if __name__ == '__main__':
    main()

    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)