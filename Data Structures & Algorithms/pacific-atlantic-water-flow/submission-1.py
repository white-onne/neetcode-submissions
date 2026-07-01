class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r<0 or c<0 or r == ROWS or c==COLS or
                heights[r][c] < prevHeight): # 가려는 곳이 더 작으면 X (오름차순이 필요함)
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # 위 또는 아래
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # 위
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # 아래

        # 왼쪽 또는 오른쪽
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        # 겹치는 부분 찾기
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res