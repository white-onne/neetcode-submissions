class Solution:
    def reverseBits(self, n: int) -> int:
        # 끝이 뭔지를 알고 그걸 붙이고 shift<<1하면 됨 맨 뒤가 1인지 아닌지는 어떻게 앎?
        # 1과 and 연산하고 그 결과값 저장하고 or 연산하면 됨
        # 32bit로 적어두기
        i = 0
        result = 0
        while i<32:
            num = n & 1
            result = result | num
            result = result<<1
            n = n >> 1
            i+=1
        result = result>>1
        return result
