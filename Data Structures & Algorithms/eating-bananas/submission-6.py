class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l<=r:
            k = (l+r)//2
            cnt_h = 0
            for i in range(len(piles)):
                cnt_h += math.ceil(piles[i]/k)
            if cnt_h <= h:
                res = k
                r = k-1
            else:
                l = k + 1
        return res