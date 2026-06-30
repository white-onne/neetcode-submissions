from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        # -1 물, 0 보물, INF 탐색 가능
        # 가장 가까운 보물 위치 값을 저장
        # grid 수정
        # 상하좌우로 이동하되, 물을 만나면 이동 불가
        # 시작점이 보물이라고 생각
        # bfs로 탐색하면서 가장 가까운 거리를 갱신해 나감
        # 0이면 안감
        # 재 탐색 시, 기존에 저장되어 있는 거리가 더 짧다면 더 이상 방문 X
        q = deque()
        n = len(grid)
        m = len(grid[0])
        visit = [[False for _ in range(m)] for _ in range(n)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i, j, 0)) # 위치, 거리 정보
        print(q)

        while q:
            x, y, cost = q.popleft()
            if visit[x][y]: # 재 방문은 하면 안됨
                continue
            visit[x][y] = True
            for mx, my in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx = mx + x
                ny = my + y
                if not(0<=nx<n and 0<=ny<m):
                    continue
                if grid[nx][ny]==0 or grid[nx][ny]==-1:
                    continue
                grid[nx][ny] = min(cost+1, grid[nx][ny])
                q.append((nx, ny, grid[nx][ny]))