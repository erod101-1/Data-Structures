# Prefix Trees
'''
Insert Word: O(1) Hash Map, Prefix Tree
Search Word: O(1) Hash Map, Prefix Tree
Search Prefix: O(1) Prefix Tree !!!!!

Applications: Auto Complete


Trie -> Tree of characters

Every Node has hash map of children 
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
    
    def startsWith(self,prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


def main():
    word = 'apple'
    tr = Trie()
    tr.insert('apple')
    assert(tr.search('apple') == True)
    assert(tr.search('app') == False)
    assert(tr.startsWith('app') == True)
    return True

if __name__ == '__main__':
    main()