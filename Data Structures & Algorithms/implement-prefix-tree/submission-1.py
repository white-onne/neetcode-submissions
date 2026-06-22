class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur =  self.root

        for c in word:
            if c not in cur.children: # 없으면 create
                cur.children[c] = TrieNode() # hashMap을 자식들로 생각할 것임
            cur = cur.children[c]
        cur.endOfWord = True # 난 끝이에요!

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        