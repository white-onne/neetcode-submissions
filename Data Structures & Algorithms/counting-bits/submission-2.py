class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        # 1의 갯수 구하기
        for i in range(1, n+1):
            cnt = 0
            while i:
                i = i & (i-1)
                cnt+=1
            result.append(cnt)
        return result