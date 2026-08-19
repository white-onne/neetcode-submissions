class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        m = len(matrix[0])
        n = len(matrix)


        startx = 0
        starty = 0
        # 위
        while m>0 and n>0:
            # 높이가 1이면
            if n==1:
                for i in range(m):
                    result.append(matrix[startx][starty+i])
                break
            if m==1:
                for i in range(n):
                    result.append(matrix[startx+i][starty])
                break
            # 위
            for i in range(m):
                result.append(matrix[startx][starty+i])
            # 오른쪽
            for i in range(n-1):
                result.append(matrix[startx+1+i][starty+m-1])
            # 아래쪽
            for i in range(m-1):
                result.append(matrix[startx+n-1][starty+m-1-i-1])
            # 왼쪽
            for i in range(n-2):
                result.append(matrix[startx+n-1-i-1][starty])
            startx+=1
            starty+=1
            m-=2
            n-=2
        return result





