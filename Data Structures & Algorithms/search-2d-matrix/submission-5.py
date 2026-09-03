class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        total_len = len(matrix)*len(matrix[0])
        right = total_len
        while left<right:
            mid = (left+right)//2
            row = mid//(len(matrix[0]))
            column = mid%(len(matrix[0]))
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                left = mid + 1
            else:
                right = mid
        row = left//(len(matrix[0]))
        column = left%(len(matrix[0]))
        if left<total_len and matrix[row][column] == target:
            return True
        return False