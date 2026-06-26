
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q=deque()
        nums=0
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j]=="1":
                    visit[i][j]=True
                    q.append([i, j])
                    nums+=1
                    while q:
                        c_x, c_y=q.pop()
                        for m_x, m_y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                            n_x, n_y=c_x+m_x, c_y+m_y
                            if 0<=n_x<len(grid) and 0<=n_y<len(grid[0]) and grid[n_x][n_y]=="1" and not visit[n_x][n_y]:
                                q.append([n_x, n_y])
                                visit[n_x][n_y]=True
        return nums
