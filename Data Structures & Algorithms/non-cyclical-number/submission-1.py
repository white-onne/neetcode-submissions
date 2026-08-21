class Solution:
    def isHappy(self, n: int) -> bool:
        already = set()
        num = n
        while num!=1 or num not in already:
            if num in already:
                return False
            already.add(num)
            total_num = 0
            for s in str(num):
                total_num+=(int(s)**2)
            num = total_num
        if num == 1:
            return True
        return False
