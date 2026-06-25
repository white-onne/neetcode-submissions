import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        nvisit = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(res: str, idx: int, x: int,y: int, visit):
            if len(res) == len(word):
                print(res)
                return True
            for mx, my in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = mx+x, my+y
                if 0<=nx<ROWS and 0<=ny<COLS and not visit[nx][ny] and word[idx] == board[nx][ny]:
                    new_visit = copy.deepcopy(visit)
                    new_visit[nx][ny] = True
                    new_str = res+board[nx][ny]
                    if dfs(new_str, idx+1, nx, ny, new_visit):
                        return True
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    new_visit = copy.deepcopy(nvisit)
                    new_visit[i][j] = True
                    if dfs(board[i][j], 1, i, j, new_visit):
                        return True
        return False