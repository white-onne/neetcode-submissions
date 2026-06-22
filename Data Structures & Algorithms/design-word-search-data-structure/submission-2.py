class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() # root에는 아무것도 없음

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: # 없으면 만들기
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True # 단어의 끝임. 중복된 단어는 이래서 못들어옴^^
        
    def search(self, word: str) -> bool: # 씨댕 조낸 어렵네
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values(): # 모든 자식을 봐야하기 때문
                        if dfs(i+1, child):
                            return True
                    return False
                else: # regular
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)     
