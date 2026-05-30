class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # key: 0~8 val: 1~9
        cols = defaultdict(set) # key: 0~8 val: 1~9
        kann = defaultdict(set) # key: 0~8 val: 1~9

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num==".": continue
                if num in rows[i] or num in cols[j] or num in kann[(i//3, j//3)]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                kann[(i//3, j//3)].add(num)
        return True