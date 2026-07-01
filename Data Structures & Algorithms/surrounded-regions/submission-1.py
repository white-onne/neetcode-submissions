from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visit = [[False for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O" and not visit[r][c]:
                    q = deque()
                    pos = [(r, c)] # O에서 X로 바꿀 위치들을 저장
                    q.append((r, c))
                    visit[r][c] = True
                    bound = False
                    while q:
                        x, y = q.popleft()
                        for mx, my in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nx,  ny = mx+x, my+y
                            if not(0<=nx<ROWS and 0<=ny<COLS):
                                bound = True
                                continue
                            if visit[nx][ny]:
                                continue
                            if board[nx][ny] == "O":
                                visit[nx][ny] = True
                                q.append((nx, ny))
                                pos.append((nx, ny))
                    if not bound: # 경계를 만난적이 없으면 X로 바꿔줌
                        for x, y in pos:
                            board[x][y] = "X"
