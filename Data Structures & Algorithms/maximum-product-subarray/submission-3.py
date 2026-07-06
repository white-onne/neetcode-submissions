class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 해설 봐도 이해가 안가네
        res = max(nums)
        
        minVal ,maxVal = 1, 1
        for num in nums:
            tmp = maxVal * num
            maxVal = max(num * maxVal, num*minVal, num)
            minVal = min(tmp, num*minVal, num)
            res = max(maxVal, minVal, res)
        return res