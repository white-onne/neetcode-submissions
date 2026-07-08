class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num, cur_num = nums[0], 0
        for num in nums:
            if cur_num<0:
                cur_num = 0
            cur_num += num
            max_num = max(max_num, cur_num)
        return max_num