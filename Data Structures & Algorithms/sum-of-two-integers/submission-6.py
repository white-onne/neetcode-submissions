class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b!=0: # carry와 b는 같다
            carry = (a&b)<<1
            a = (a^b) & mask # 음수 연산을 위해
            b = carry & mask # 음수 연산을 위해

        return a if a<=max_int else ~(a^mask)
            