class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 오른쪽 혹은 아래쪽으로 갈 수 있음
        # 갈 수 있는 unique한 path들 갯수를 구하기
        # 진짜 어드밴스네
        row = [1] * n
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]