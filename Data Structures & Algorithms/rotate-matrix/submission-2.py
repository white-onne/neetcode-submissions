class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        result = []
        for i in range(n):
            result.append([0]*n)

        def rotation(startx, starty, nation):
            # 위
            top = matrix[startx][starty:starty+nation]
            # 아래
            bottom =  matrix[startx+nation-1][starty:starty+nation]
            # 왼쪽
            left = [0]*nation
            for i in range(startx, startx+nation):
                left[i-startx] = matrix[i][starty]
            # 오른쪽
            right = [0] * nation
            for i in range(startx, startx + nation):
                right[i-startx] = matrix[i][starty+nation-1]
            # new matrix에 쓰기
            # 위 -> 오른쪽
            for i in range(nation):
                result[startx+i][starty+nation-1] = top[i]
            # 오른쪽 -> 아래
            for i in range(nation):
                result[startx+nation-1][starty+i] = right[nation-i-1]
            # 아래 -> 왼쪽
            for i in range(nation):
                result[startx+i][starty] = bottom[i]
            # 왼쪽 -> 위
            for i in range(nation):
                result[startx][starty+i] = left[nation-i-1]
        matrix_num = n
        cnt = 0
        while matrix_num>1:
            rotation(cnt, cnt, matrix_num)
            matrix_num-=2
            cnt+=1
        if matrix_num == 1:
            result[n//2][n//2] = matrix[n//2][n//2]
        # matrix에 쓰기
        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]
        return
