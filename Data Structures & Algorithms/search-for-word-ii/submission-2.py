class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        cur = self # 나 자신이 cur이여
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # BruteForce하면 N*N*M
        # Trie를 사용해 시간복잡도를 낮춘다.
        # words로 Trie를 만든 다음, 그래프 탐색 범위를 좁혀 나감
        # 백트래킹에선 탐색 범위를 줄여나가는 것이 중요하다.
        # 그래프 탐색할 때 해당 단어들 모음 있는지 아닌지 Prefix 그래프를 통해 확인하고 없으면 그쪽으로는 탐색안하는 것
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set() # :) 같은 문자를 또 추가하면 안됨 왜냐하면 조건에서 그렇게 말함 하지말래
        def dfs(r, c, node, word):
            if r<0 or c<0 or r==ROWS or c==COLS or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            # backtracking임으로
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
