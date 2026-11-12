class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])

        result = 0
        banana_num = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    banana_num += 1
                if grid[i][j] == 2:
                    q.append((i, j))


        while banana_num>0 and q:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                for mx, my in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx = mx + x
                    ny = my + y
                    if (nx in range(len(grid))
                        and ny in range(len(grid[0]))
                        and grid[nx][ny] == 1
                    ):
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        banana_num -= 1
            result +=1

        return result if banana_num == 0 else -1