class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_1 = [0] * (len(nums)-1) # 0~(n-2)
        dp_2 = [0] * (len(nums)-1) # 1~(n-1)

        for i in range(len(nums)-1):
            dp_1[i] = nums[i]
        if len(nums)>3:
            dp_1[1] = max(dp_1[0], dp_1[1])
        
        for i in range(1, len(nums)):
            dp_2[i-1] = nums[i]
        if len(nums)>2:
            dp_2[1] = max(dp_2[0], nums[2])
        
        # dp_1: 0~(n-2)
        for i in range(2, len(nums)-1):
            dp_1[i] = max(dp_1[i-2]+dp_1[i], dp_1[i-1])
        # dp_2: 1~(n-1)
        for i in range(2, len(nums)-1):
            dp_2[i] = max(dp_2[i-2]+dp_2[i], dp_2[i-1])

        if len(nums)==1: return nums[0]
        return max(dp_1[len(dp_1)-1],dp_1[len(dp_1)-2], dp_2[len(dp_2)-1],dp_2[len(dp_2)-2])