class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = [] # i
        zero_column = [] # j
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_column.append(j)
        # zero로 설정
        # row(i) ~ j
        while zero_row:
            ik = zero_row.pop()
            for i in range(len(matrix[0])):
                matrix[ik][i] = 0
        while zero_column:
            jk = zero_column.pop()
            for i in range(len(matrix)):
                matrix[i][jk] = 0

        return
        